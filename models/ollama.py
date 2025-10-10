from tools import change_project_directory, get_directory_tree, create_directory, create_file_and_insert_content, get_file_content
from langchain_ollama import ChatOllama

llm = ChatOllama(model="llama3.1:8b", temperature=0).bind_tools([get_directory_tree, create_directory, create_file_and_insert_content, get_file_content, change_project_directory])