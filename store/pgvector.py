from langchain_postgres import PGVectorStore, PGEngine
from .embeddings.ollama import embeddings
import os

engine = PGEngine.from_connection_string(os.getenv("DATABASE_URL", "postgresql://postgres:password@localhost:5432/postgres"))

vector_store = PGVectorStore.create_sync(engine=engine, 
                                    embedding_service=embeddings, 
                                    table_name=os.getenv("VECTOR_TABLE_NAME", "vectors"), 
                                    metadata_json_column="metadata")

