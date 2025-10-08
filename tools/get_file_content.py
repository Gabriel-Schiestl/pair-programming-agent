from langchain.tools import tool

@tool
def get_file_content(file_path: str) -> str:
    """Get the content of a file given its path."""
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        return content
    except Exception as e:
        return f"Error reading file: {e}"