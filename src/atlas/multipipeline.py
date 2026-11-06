from atlas.document_loader import discover_documents
from atlas.reader import read_document
from atlas.chunker import chunk_text
from atlas.embedder import get_embedding
from atlas.search import search_vectors
from pathlib import Path


def search_documents_vector(folder_path, query_text, chunk_size, top_k=3):
    document_list = discover_documents(folder_path)
    if not document_list:
        return None
    print(f'Generating embedding for query: {query_text}...')
    query_vector = get_embedding(query_text)
    
    if not query_vector:
        print('Failed to generate query embedding.')
        return None
    
    all_chunk_data = []
    
    for file_path in document_list:
        document_text = read_document(file_path)
        if document_text is None:
            continue
        chunks = chunk_text(document_text, chunk_size)
        print(f'Procesisng {file_path.name} ({len(chunks)} chunks)...')
        
        for chunk in chunks:
            chunk_vec = get_embedding(chunk)
            if chunk_vec:
                all_chunk_data.append({
                    'text' : chunk,
                    'vector' : chunk_vec,
                    'source' : file_path.name
                })
    if not all_chunk_data:
        return None
    searchable_data = [(item['text'], item['vector']) for item in all_chunk_data]
    
    print ('Ranking results via Cosine Similarity...')
    
    top_results = search_vectors(query_vector, searchable_data, top_k=top_k)
    
    final_results = []
    
    for result in top_results:
        source_name = next(item['source'] for item in all_chunk_data if item['text'] == result['chunk'])
        final_results.append({
            'score': result['score'],
            'chunk': result['chunk'],
            'source': source_name
        })
    return final_results