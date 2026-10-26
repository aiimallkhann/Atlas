from pathlib import Path

def discover_documents(folder_path):
    files = []
    folder_path = Path(folder_path)
    if folder_path.is_dir():
        for file_path in folder_path.glob('*.txt'):
            files.append(file_path)
    else:
        return None
    return files