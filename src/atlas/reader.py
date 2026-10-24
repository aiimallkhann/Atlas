from pathlib import Path

def read_document(pth):
    if pth.is_file():
        print(f'Your path {pth.resolve()} is valid')
    else:
        print(f'invalid path {pth.resolve()}')

file = Path('D:/New Folder/My Works/The Ache to Express A Meditation on.txt')

read_document(file)