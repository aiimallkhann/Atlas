from atlas.reader import read_document
from atlas.search import search_text
from atlas.analyzer import analyze_text
from atlas.chunker import chunk_text
from pathlib import Path

def search_do (file_path, query, chunk_size):
    path = Path(file_path)
    print (path)
search_do('C:/', 'hello', 5)