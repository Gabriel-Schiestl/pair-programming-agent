from langchain.tools import tool

@tool
def create_directory(path: str) -> str:
    """Create a directory at the specified path, including any necessary parent directories.

    This function creates the directory recursively if it does not exist. If the directory
    already exists, it does nothing and returns a success message. Useful for ensuring
    directory structures are in place before creating files or other operations.

    Args:
        path (str): The full path of the directory to create.

    Returns:
        str: A success message if created, or an error message if failed.
    """
    import os
    try:
        os.makedirs(path, exist_ok=True)
        return f"Directory created at: {path}"
    except Exception as e:
        return f"Error creating directory: {e}"