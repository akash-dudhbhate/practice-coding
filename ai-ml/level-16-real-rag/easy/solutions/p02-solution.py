"""Level 16 — Real RAG — Easy P02 Solution"""

import numpy as np


def cosine_all(query_vec, doc_matrix):
    """Cosine similarity of one query vector vs every row of doc_matrix.

    Returns a 1-D np.array of length n_docs.
    """
    q = query_vec.toarray() if hasattr(query_vec, "toarray") else query_vec
    D = doc_matrix.toarray() if hasattr(doc_matrix, "toarray") else doc_matrix
    q = np.asarray(q, dtype=float).ravel()
    D = np.asarray(D, dtype=float)
    if D.ndim == 1:
        D = D.reshape(1, -1)
    qn = np.linalg.norm(q)
    q = q / qn if qn else q
    dn = np.linalg.norm(D, axis=1, keepdims=True)
    dn[dn == 0] = 1.0
    return (D / dn) @ q


if __name__ == "__main__":
    D = np.array([[1., 0.], [0., 1.], [1., 1.]])
    q = np.array([1., 0.])
    print(cosine_all(q, D))
