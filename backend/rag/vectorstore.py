from langchain_community.vectorstores import Chroma

from rag.embeddings import get_embeddings


def create_vectorstore(chunks):

    if not chunks:
        print("NO CHUNKS FOUND")
        return None


    db = Chroma.from_documents(
        documents=chunks,
        embedding=get_embeddings(),
        persist_directory="vector_db"
    )


    db.persist()


    print("VECTOR DATABASE CREATED")


    return db