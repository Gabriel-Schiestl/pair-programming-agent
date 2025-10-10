from langchain.tools import tool
import os

@tool
def create_file_and_insert_content(file_path: str, content: str) -> str:
    """Create a new file at the specified path with the given content, creating parent directories if needed.

    Overwrites the file if it already exists. Ensures the directory structure exists
    before writing the file. Useful for generating code files, configuration files, or any text content.

    Args:
        file_path (str): The full path including filename where the file will be created.
        content (str): The text content to write into the file.

    Returns:
        str: A success message with the file path, or an error message if creation failed.
    """
    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        with open(file_path, 'w') as file:
            file.write(content)
        
        return f"File created at {file_path}"
    except Exception as e:
        return f"Error creating file at {file_path}: {e}"
