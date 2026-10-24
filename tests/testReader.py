from atlas.reader import read_document
from pathlib import Path

file = Path('D:/New Folder/My Works/The Ache to Express A Meditation on.txt')

result = read_document(file)
print(result)