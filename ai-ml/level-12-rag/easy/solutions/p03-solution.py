"""Level 12 Rag — Easy P03 Solution"""

def solve():
    text = "Machine learning is a subset of artificial intelligence. It uses algorithms to learn patterns from data. Deep learning is a type of machine learning that uses neural networks with many layers."
    def chunk_text(text, chunk_size=50, overlap=10):
        chunks = []
        start = 0
        while start < len(text):
            end = start + chunk_size
            chunks.append(text[start:end])
            start = end - overlap
        return chunks
    chunks = chunk_text(text)
    print(f"Original text ({len(text)} chars):")
    print(text)
    print(f"\nChunks ({len(chunks)}):")
    for i, chunk in enumerate(chunks):
        print(f"  {i}: {chunk}")
    return chunks

if __name__ == "__main__":
    solve()