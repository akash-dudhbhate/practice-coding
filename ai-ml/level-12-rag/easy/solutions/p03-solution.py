"""Level 12 — RAG Systems — Easy P03 Solution"""

def chunk_text(text, chunk_size, overlap):
    step = chunk_size - overlap
    chunks = []
    for i in range(0, len(text), step):
        chunk = text[i:i + chunk_size]
        if chunk:
            chunks.append(chunk)
        if i + chunk_size >= len(text):
            break
    return chunks

if __name__ == "__main__":
    text = "Machine learning is a subset of artificial intelligence. It uses algorithms to learn patterns from data. Deep learning is a type of machine learning that uses neural networks with many layers."
    chunks = chunk_text(text, 50, 10)
    print(len(chunks))
    for i, c in enumerate(chunks):
        print(f"  {i}: {c}")
