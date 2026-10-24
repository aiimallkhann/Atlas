def search_text(chunks, query):
    query = query.lower()
    chunks = [chunk.lower() for chunk in chunks]
    # split_chunks = chunks.split()
    # split_query = query.split()
    for chunk in chunks:
        found = False
        if query in chunk:
            found = True
            print(f'Found Query {query} in chunk.\n')
            print(chunk)
            return
        print('Query not found.\n')
        return False
    return
chunks = ['this is the first chunk', 'this is the second chunk']
search_text(chunks, 'nigga')