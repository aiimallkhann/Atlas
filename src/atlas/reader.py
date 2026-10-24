from pathlib import Path

def read_document(pth):
    if pth.is_file():
        with pth.open(encoding='utf-8') as f:
            return(f.read())
    else:
        return None;
