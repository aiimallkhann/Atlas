from pathlib import Path

def read_document(path):
    path = Path(path)

    if not path.is_file():
        return None

    with path.open(encoding="utf-8") as file:
        return file.read()