import numpy as np


def cosine_similarity(vec1, vec2):
    vc1 = np.array(vec1)
    vc2 = np.array(vec2)

    norm_vc1 = np.linalg.norm(vc1)
    norm_vc2 = np.linalg.norm(vc2)

    if norm_vc1 == 0 or norm_vc2 == 0:
        return 0.0
    return float(np.dot(vc1, vc2) / (norm_vc1 * norm_vc2))


def search_vectors(query_vector, chunk_data, top_k=5):
    results = []

    for index, (chunk_text, chunk_vector) in enumerate(chunk_data):
        if chunk_vector is None or len(chunk_vector) == 0:
            continue
        score = cosine_similarity(query_vector, chunk_vector)
        results.append({
            'score': score,
            'chunk': chunk_text,
            'index': index
        })
        
    results.sort(key=lambda x: x['score'], reverse=True)
    return results[:top_k]