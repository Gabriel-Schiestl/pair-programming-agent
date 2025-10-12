from langchain_ollama import OllamaEmbeddings
import os

embeddings = OllamaEmbeddings(model=os.getenv("OLLAMA_EMBEDDING_MODEL", "nomic-embed-text"))