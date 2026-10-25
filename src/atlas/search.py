def search_text(chunks, query):
    query_words = query.lower().split()
    results = []

    if not query_words:
        return []

    for chunk in chunks:
        chunk_words = chunk.lower().split()
        score = sum(1 for word in query_words if word in chunk_words)

        if score > 0:
            results.append((score, chunk))

    ranked_results = sorted(results, key=lambda result: result[0], reverse=True)

    return ranked_results