def chunk_text(text, chunk_size=40, overlap=10):
    if overlap < 0 or chunk_size <= 0:
        raise ValueError("chunk_size must be greater than 0")

    words = text.split()
    chunks = []
    step = chunk_size - overlap
    
    for i in range(0, len(words), step):
        chunks.append(" ".join(words[i:i + chunk_size]))
        if i + chunk_size >= len(words):
            break
            
    return chunks