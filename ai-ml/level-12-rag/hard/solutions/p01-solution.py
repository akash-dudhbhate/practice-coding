"""Level 12 Rag — Hard P01 Solution"""

def solve():
    class RAGPipeline:
        def __init__(self):
            self.documents = []
            self.embeddings = []
        def index(self, documents):
            for doc in documents:
                self.documents.append(doc)
                self.embeddings.append(self.embed(doc))
        def embed(self, text):
            import numpy as np
            np.random.seed(hash(text) % 2**32)
            return np.random.randn(384)
        def retrieve(self, query, top_k=3):
            import numpy as np
            query_emb = self.embed(query)
            scores = [np.dot(query_emb, emb) / (np.linalg.norm(query_emb) * np.linalg.norm(emb)) for emb in self.embeddings]
            top_idx = np.argsort(scores)[-top_k:][::-1]
            return [(self.documents[i], scores[i]) for i in top_idx]
        def generate(self, query, context):
            return f"Based on: {context[0][0]}\nAnswer: {query} is related to machine learning."
    rag = RAGPipeline()
    rag.index(["ML is great", "Deep learning is powerful", "Data science rocks"])
    results = rag.retrieve("What is ML?")
    answer = rag.generate("What is ML?", results)
    print(answer)
    return rag

if __name__ == "__main__":
    solve()