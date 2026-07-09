from rag.loader import load_pdf
from rag.splitter import split_documents
from rag.vectorstore import create_vectorstore
from services.ollama_service import generate_response


def upload_document(file_path):

    print("========== RAG START ==========")

    documents = load_pdf(file_path)

    print("PDF LOADED:", len(documents))


    chunks = split_documents(documents)

    print("CHUNKS CREATED:", len(chunks))


    if len(chunks) == 0:
        return "PDF has no readable text"


    create_vectorstore(chunks)

    print("========== RAG DONE ==========")


    return "Document processed successfully"



def ask_document(question):

    response = generate_response(question)

    return response