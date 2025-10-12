from langchain_core.documents import Document
from store.pgvector import vector_store
import json

with open('documents.json', 'r') as f:
    data = json.load(f)

documents = []

for doc in data:
    pattern = doc.get("pattern", "")
    content = doc.get("content", "")
    language = str(doc.get("language", "")).upper()
    document = Document(page_content=pattern, metadata={"content_text": content, "language": language})
    documents.append(document)

vector_store.add_documents(documents)

