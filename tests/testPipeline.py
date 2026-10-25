from atlas.pipeline import search_document
from pathlib import Path

path = r'D:\New folder\My Works\The Ache to Express A Meditation on.txt'
query = 'Ayesha,'
chunk_size = 1

print(search_document(path, query, chunk_size))