def chunk_text(text, chunk_size):
    if chunk_size <= 0:
        raise ValueError("chunk_size must be greater than 0")

    words = text.split()
    chunks = []

    for i in range(0, len(words), chunk_size):
        chunk = " ".join(words[i:i + chunk_size])
        chunks.append(chunk)

    return chunks
