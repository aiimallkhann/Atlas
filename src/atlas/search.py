import re

def search_text(chunks, query):
    query_words = re.findall(r"\b\w+\b", query.lower())
    results = []

    if not query_words:
        return []

    for chunk in chunks:
        chunk_words = re.findall(r"\b\w+\b", chunk.lower())
        score = sum(1 for word in query_words if word in chunk_words)

        if score > 0:
            results.append((score, chunk))

    ranked_results = sorted(results, key=lambda result: result[0], reverse=True)

    return ranked_results