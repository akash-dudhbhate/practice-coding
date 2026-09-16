"""Level 16 — Real RAG — Easy P03 Solution"""


def chunk_text(text, size=100, overlap=20):
    """Split `text` into overlapping chunks with offset metadata.

    Returns [{"id": i, "text": str, "start": int, "end": int}, ...]
    where text[start:end] == chunk text.
    """
    step = max(1, size - overlap)
    chunks = []
    start = 0
    while start < len(text):
        end = min(start + size, len(text))
        chunks.append({"id": len(chunks), "text": text[start:end],
                       "start": start, "end": end})
        if end >= len(text):
            break
        start += step
    return chunks


if __name__ == "__main__":
    for c in chunk_text("abcdefghijklmnopqrst" * 15, 100, 20):
        print(c["id"], c["start"], c["end"], len(c["text"]))
