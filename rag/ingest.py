from pathlib import Path

from langchain_core.documents import Document

from rag.vectordb import get_vector_db


SNAPSHOT_FOLDER = "snapshots"


def ingest_snapshots():

    db = get_vector_db()

    documents = []

    snapshot_files = (
        Path(SNAPSHOT_FOLDER)
        .glob("*.txt")
    )

    for file in snapshot_files:

        content = file.read_text(
            encoding="utf-8"
        )

        doc = Document(
            page_content=content,
            metadata={
                "source": str(file)
            }
        )

        documents.append(doc)

    if documents:

        db.add_documents(documents)

        print(
            f"Added {len(documents)} "
            f"documents to ChromaDB"
        )