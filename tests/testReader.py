from atlas.reader import read_document
from pathlib import Path

file = Path('data/documents/sample.txt')

result = read_document(file)