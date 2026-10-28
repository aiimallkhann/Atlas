from atlas.document_loader import discover_documents

def search_document(folder_path, query, chunk_size):
    documents_list = []
    documents_list = discover_documents(folder_path)
    if documents_list is None:
        return None
    else:
        return documents_list