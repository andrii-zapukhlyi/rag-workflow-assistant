from langchain_core.documents import Document
from langchain_huggingface.embeddings import HuggingFaceEndpointEmbeddings
from langchain_qdrant import QdrantVectorStore

from config.settings import HF_API_TOKEN
from agents.qa_agent.chunker import chunk_and_prepare_metadata
from agents.qa_agent.confluence_client import get_all_pages


def build_vector_db(url: str, collection: str) -> None:
    embedding = HuggingFaceEndpointEmbeddings(
        model="sentence-transformers/all-MiniLM-L6-v2",
        task="feature-extraction",
        huggingfacehub_api_token=HF_API_TOKEN,
    )

    documents = get_all_pages()
    chunks, metadata = chunk_and_prepare_metadata(documents)

    docs = [
        Document(page_content=chunk, metadata=meta)
        for chunk, meta in zip(chunks, metadata)
    ]

    QdrantVectorStore.from_documents(
        docs,
        embedding=embedding,
        url=url,
        collection_name=collection,
    )
