from atlas.reader import read_document
from atlas.search import search_text
from atlas.analyzer import analyze_text
from atlas.chunker import chunk_text
from pathlib import Path

def search_document (file_path, query, chunk_size):
    path = Path(file_path)
    check = read_document(path)
    if check is None:
        return None
    chunks = chunk_text(check, chunk_size)
    results = search_text(chunks, query)
    stats = analyze_text(check)
    return {
        'statistics': stats,
        'results': results,
        'source': path.name
    }
