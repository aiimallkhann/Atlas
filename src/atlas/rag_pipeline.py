from atlas.multipipeline import search_documents_vector
from atlas.generator import build_prompt

def ask_atlas(folder_path, query,chunk_size=50):
    result = search_documents_vector(folder_path, query, chunk_size)
    if not result:
        return 'No relevant information found or invalid search parameters.'
    final_prompt = build_prompt(query, result)
    return final_prompt