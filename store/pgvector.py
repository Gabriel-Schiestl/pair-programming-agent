
from langchain_postgres import PGVectorStore, PGEngine
from .embeddings.ollama import embeddings
import os

engine = PGEngine.from_connection_string(
    os.getenv("DATABASE_URL", "postgresql+psycopg://postgres:postgres@172.24.224.1:5432/ppg")
)

vector_store = PGVectorStore.create_sync(
    engine=engine,
    embedding_service=embeddings,
    table_name=os.getenv("VECTOR_TABLE_NAME", "documents"),
    content_column=os.getenv("CONTENT_COLUMN", "pattern"),
    metadata_columns=["content_text", "language"],
    metadata_json_column=os.getenv("METADATA_JSON_COLUMN", "metadata"),
    id_column=os.getenv("ID_COLUMN", "id"),
)

