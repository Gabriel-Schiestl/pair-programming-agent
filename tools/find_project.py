from langchain.tools import tool
from pathlib import Path
import os

@tool
def find_project(project: str) -> str:
    """
    Find a project in the projects directories. 
    If found, return the full path. If not found, return 'Project not found'.
    """

    projects_dirs = os.getenv("PROJECTS_DIRS", "github,gitlab").split(",")
    path = Path(os.getenv("FULLPATH", "/home/schiestl/workspace"))
    
    for dir in projects_dirs:
        full_path = path / dir / project

        exists = full_path.exists()
        if exists:
            return str(full_path)

    return "Project not found"
