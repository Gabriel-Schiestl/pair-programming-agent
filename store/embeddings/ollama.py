from langchain_ollama import OllamaEmbeddings
import os

embeddings = OllamaEmbeddings(model=os.getenv("OLLAMA_EMBEDDING_MODEL", "llama3.1:8b"))