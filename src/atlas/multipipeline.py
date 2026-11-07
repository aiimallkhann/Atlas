import json
from pathlib import Path
from atlas.document_loader import discover_documents
from atlas.reader import read_document
from atlas.chunker import chunk_text
from atlas.embedder import get_embedding
from atlas.search import search_vectors

# This is our local "database" file
VECTOR_STORE_FILE = "vector_store.json"

def build_index(folder_path, chunk_size):
    """
    PHASE 1: Reads, chunks, embeds, and saves to disk. 
    You only run this when you add a new document.
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

    # Save the expensive math to the hard drive
    with open(VECTOR_STORE_FILE, "w", encoding="utf-8") as f:
        json.dump(all_chunk_data, f)
        
    print(f"\nSUCCESS: Saved {len(all_chunk_data)} vectorized chunks to {VECTOR_STORE_FILE}.")
    return True


def search_index(query_text, top_k=3):
    """
    PHASE 2: Loads the database, embeds the query, and searches instantly.
    """
    if not query_text or not query_text.strip():
        return []

    # Check if the database exists before trying to search it
    if not Path(VECTOR_STORE_FILE).is_file():
        print(f"Error: {VECTOR_STORE_FILE} not found. Please build the index first.")
        return None

    # Instantly load all pre-computed vectors into memory
    with open(VECTOR_STORE_FILE, "r", encoding="utf-8") as f:
        all_chunk_data = json.load(f)

    print(f'Generating embedding for query: {query_text}...')
    query_vector = get_embedding(query_text)

    if not query_vector:
        print('Failed to generate query embedding.')
        return None

    # Format for search.py using your exact structure
    searchable_data = [(item['text'], item['vector']) for item in all_chunk_data]

    print('Ranking results via Cosine Similarity...')
    top_results = search_vectors(query_vector, searchable_data, top_k=top_k)

    # Return exactly the same way, using your O(1) index lookup
    return [
        {
            'score': result['score'],
            'chunk': result['chunk'],
            'source': all_chunk_data[result['index']]['source']
        }
        for result in top_results
    ]