from rag.vectorstore import load_vectorstore


def retrieve(query: str, k: int = 4):

    db = load_vectorstore()

    return db.similarity_search(query, k=k)