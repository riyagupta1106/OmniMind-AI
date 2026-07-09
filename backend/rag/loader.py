from langchain_community.document_loaders import PyMuPDFLoader


def load_pdf(path):

    loader = PyMuPDFLoader(path)

    pages = loader.load()


    print(
        "TOTAL PDF PAGES:",
        len(pages)
    )


    for page in pages:
        print(
            "TEXT LENGTH:",
            len(page.page_content)
        )


    return pages