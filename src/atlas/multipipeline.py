from atlas.document_loader import discover_documents
from atlas.reader import read_document
from atlas.chunker import chunk_text
from atlas.search import search_text
from pathlib import Path

def search_document(folder_path, query, chunk_size):
    result_chunks_docs = []
    documents_list = discover_documents(folder_path)
    if documents_list is None:
        return None
    for file_path in documents_list:
        document_text = read_document(file_path)
        if document_text is None:
            continue
        document_chunks = chunk_text(document_text, chunk_size)
        results = search_text(document_chunks, query)
        print('searching ', file_path.name)
        print('results ', results)
        result_chunks_docs.extend(document_chunks)
    return result_chunks_docs

path = Path(r'D:\New folder\My Works')
search_document(path, 'express', 3)