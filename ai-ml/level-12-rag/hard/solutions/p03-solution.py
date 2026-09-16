"""Level 12 Rag — Hard P03 Solution"""

def solve():
    class AdvancedRAG:
        def __init__(self):
            self.documents = []
        def rewrite_query(self, query):
            # Expand query with synonyms
            expansions = {'ML': 'machine learning', 'AI': 'artificial intelligence'}
            for abbr, full in expansions.items():
                query = query.replace(abbr, full)
            return query
        def multi_hop_retrieve(self, query):
            # First hop: get initial docs
            hop1 = self.retrieve(query)
            # Second hop: use first results to refine
            refined = self.retrieve(hop1[0][0])
            return refined
        def retrieve(self, query):
            # Dummy retrieval
            return [("Doc about " + query, 0.9)]
    rag = AdvancedRAG()
    query = "What is ML?"
    rewritten = rag.rewrite_query(query)
    print(f"Original: {query}")
    print(f"Rewritten: {rewritten}")
    results = rag.multi_hop_retrieve(rewritten)
    print(f"Results: {results}")
    return rag

if __name__ == "__main__":
    solve()