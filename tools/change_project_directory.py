from state import AgentState
from pathlib import Path
import os
from langchain_core.messages import AIMessage
from langchain.tools import tool

@tool
def change_project_directory(directory: str) -> str:
    """
    Change the current working directory of the agent. Useful for changing the project directory when asked by the user.

    Args:
        directory (str): The new directory to change to. Should be just the new project directory name, e.g., 'my_project'.
    """
    if not directory:
        return "Error: No directory specified"
    
    projects_dirs = os.getenv("PROJECTS_DIRS", "github,gitlab").split(",")
    path = Path(os.getenv("FULLPATH", "/home/schiestl/workspace"))
    
    for dir in projects_dirs:
        full_path = path / dir / directory
        if full_path.exists() and full_path.is_dir():
            return str(full_path)
    
    return f"Error: Invalid directory {directory}"