from state import AgentState
from langchain_core.messages import AIMessage, ToolMessage

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