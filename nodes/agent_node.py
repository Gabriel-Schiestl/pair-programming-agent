from state import AgentState
from langchain_core.messages import AIMessage
from prompts import system_message
from models import llm

def agent_node(state: AgentState) -> dict:
    current_dir = state.get('current_directory', 'Not set')
    context_message = AIMessage(content=f"Current working directory: {current_dir}")
    messages = [system_message, context_message] + state["messages"]
    response = llm.invoke(messages)

    return {"messages": [response]}