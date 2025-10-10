from langchain_ollama import ChatOllama
from langchain.schema import SystemMessage
from tools import agent_tools, change_project_directory, get_directory_tree, create_directory, create_file_and_insert_content, get_file_content
from langgraph.graph import StateGraph
from state import AgentState
from langchain_core.messages import AIMessage, HumanMessage, ToolMessage
from langgraph.prebuilt import tools_condition

llm = ChatOllama(model="llama3.1:8b", temperature=0).bind_tools([get_directory_tree, create_directory, create_file_and_insert_content, get_file_content, change_project_directory])

system_message = SystemMessage(content="""
    You are a pair programming assistant. You have tools to interact with directories and files.
    If the current_directory is not set in the state, call change_project_directory with the user's input to set the working directory.
    Use current_directory for all file operations unless explicitly instructed to change it.
    Use tools to interact with the file system (e.g., create files, read content, list directories).
    Respond clearly, confirm actions, and continue reasoning until the problem is solved.
""")

def agent_node(state: AgentState) -> dict:
    current_dir = state.get('current_directory', 'Not set')
    context_message = AIMessage(content=f"Current working directory: {current_dir}")
    messages = [system_message, context_message] + state["messages"]
    response = llm.invoke(messages)

    return {"messages": [response]}

def change_directory_node(state: AgentState) -> dict:
    last_message = state["messages"][-1]
    if isinstance(last_message, ToolMessage) and last_message.name == "change_project_directory":
        if last_message.content.startswith("Error"):
            return {"messages": [AIMessage(content=last_message.content)]}
        new_directory = last_message.content.replace("Changed directory to ", "")
        return {
            "current_directory": new_directory,
            "messages": [AIMessage(content=f"Directory changed to {new_directory}")]
        }
    return state

builder = StateGraph(AgentState)

builder.add_node("agent", agent_node)
builder.set_entry_point("agent")
builder.add_node("tools", agent_tools)
builder.add_node("change_directory", change_directory_node)
builder.add_conditional_edges("agent", tools_condition)
builder.add_edge("tools", "change_directory")
builder.add_edge("change_directory", "agent")
builder.set_finish_point("agent")

graph = builder.compile()