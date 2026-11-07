import json
from pathlib import Path
from atlas.document_loader import discover_documents
from atlas.reader import read_document
from atlas.chunker import chunk_text
from atlas.embedder import get_embedding
from atlas.search import search_vectors

# The Two-Tier Database System
BASE_STORE_FILE = "base_vector_store.json"
USER_STORE_FILE = "user_vector_store.json"

def build_index(folder_path, chunk_size, is_base=False):
    """
    PHASE 1: Reads, chunks, embeds, and saves to disk.
    If is_base=True, saves to the public base store.
    If is_base=False, saves to the private user store.
    """
    document_list = discover_documents(folder_path)
    if not document_list:
        print("No documents found.")
        return False

    all_chunk_data = []

    for file_path in document_list:
        document_text = read_document(file_path)
        if document_text is None:
            continue
            
        chunks = chunk_text(document_text, chunk_size)
        print(f'Processing {file_path.name} ({len(chunks)} chunks)...')

        for chunk in chunks:
            chunk_vec = get_embedding(chunk)
            if chunk_vec:
                all_chunk_data.append({
                    'text': chunk,
                    'vector': chunk_vec,
                    'source': file_path.name
                })

    if not all_chunk_data:
        print("No embeddings generated.")
        return False

    # Decide which database file to save to!
    target_file = BASE_STORE_FILE if is_base else USER_STORE_FILE

    with open(target_file, "w", encoding="utf-8") as f:
        json.dump(all_chunk_data, f)
        
    print(f"\nSUCCESS: Saved {len(all_chunk_data)} vectorized chunks to {target_file}.")
    return True


def search_index(query_text, top_k=3):
    """
    PHASE 2: Loads BOTH databases (if they exist), merges them, and searches.
    """
    if not query_text or not query_text.strip():
        return []

    all_chunk_data = []

    # 1. Load the Base Store (Atlas's built-in knowledge)
    if Path(BASE_STORE_FILE).is_file():
        with open(BASE_STORE_FILE, "r", encoding="utf-8") as f:
            all_chunk_data.extend(json.load(f))
            print(f"[DEBUG] Loaded base knowledge.")

    # 2. Load the User Store (Personal private files)
    if Path(USER_STORE_FILE).is_file():
        with open(USER_STORE_FILE, "r", encoding="utf-8") as f:
            all_chunk_data.extend(json.load(f))
            print(f"[DEBUG] Loaded user personal knowledge.")

    # 3. Check if we actually loaded anything at all
    if not all_chunk_data:
        print("Error: No databases found. Please build an index first.")
        return None

    print(f'Generating embedding for query: {query_text}...')
    query_vector = get_embedding(query_text)

    if not query_vector:
        print('Failed to generate query embedding.')
        return None

    searchable_data = [(item['text'], item['vector']) for item in all_chunk_data]

    print('Ranking results via Cosine Similarity...')
    top_results = search_vectors(query_vector, searchable_data, top_k=top_k)

    return [
        {
            'score': result['score'],
            'chunk': result['chunk'],
            'source': all_chunk_data[result['index']]['source']
        }
        for result in top_results
    ]