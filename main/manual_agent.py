from tools import agent_tools
from langgraph.graph import StateGraph
from state import AgentState
from langgraph.prebuilt import tools_condition
from nodes import agent_node, change_directory_node

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