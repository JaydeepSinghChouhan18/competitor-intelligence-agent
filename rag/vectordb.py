from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

from config import CHROMA_DB_PATH


EMBEDDING_MODEL = (
    "sentence-transformers/all-MiniLM-L6-v2"
)


def get_embedding_model():

    return HuggingFaceEmbeddings(
        model_name=EMBEDDING_MODEL
    )


def get_vector_db():

    embeddings = get_embedding_model()

    db = Chroma(
        persist_directory=CHROMA_DB_PATH,
        embedding_function=embeddings
    )

    return db