from langchain_ollama import ChatOllama
from langchain.schema import SystemMessage
from langgraph.prebuilt import create_react_agent
from tools import get_file_content, get_directory_tree, find_project, create_file_and_insert_content, create_directory

llm = ChatOllama(model="llama3.1:8b", temperature=0)

system_message = SystemMessage(content="""
        You are a pair programming assistant. You have many tools at your disposal to interact with directories and files.
        The user will ask you some help with coding, and you will assist them. You can write code for them, and you can also
        modify files and directories. You can also read files to understand their content.
        Use the tools you have at your disposal to interact with the file system. Do not end your reasoning while you couldn't solve the problem yet
""")

agent_tools = [get_file_content, get_directory_tree, find_project, create_file_and_insert_content, create_directory]

graph = create_react_agent(model=llm, prompt=system_message, tools=agent_tools)

