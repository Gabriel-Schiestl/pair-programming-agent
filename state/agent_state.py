from typing import TypedDict, Annotated
from langchain_core.messages import AnyMessage, AIMessage
from langgraph.graph import add_messages
from pathlib import Path
import os

class AgentState(TypedDict):
    current_directory: Annotated[str, "The current working directory of the agent."]
    messages: Annotated[list[AnyMessage], add_messages]