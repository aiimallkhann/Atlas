from pathlib import Path

def discover_documents(folder_path):
    files = []
    folder_path = Path(folder_path)
    
    print(f'[DEBUG] Checking if folder exists: {folder_path.resolve()} -> {folder_path.is_dir()}')
    
    if folder_path.is_dir():
        for file_path in folder_path.glob('*.txt'):
            files.append(file_path)
        print(f'[DEBUG] Found {len(files)} .txt files in the folder.')
    else:
        return None
    return files