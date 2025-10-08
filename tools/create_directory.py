from langchain.tools import tool

@tool
def create_directory(path: str) -> str:
    """Create a directory at the specified path."""
    import os
    try:
        os.makedirs(path, exist_ok=True)
        return f"Directory created at: {path}"
    except Exception as e:
        return f"Error creating directory: {e}"