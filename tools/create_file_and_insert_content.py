from langchain.tools import tool
import os

@tool
def create_file_and_insert_content(file_path: str, content: str) -> str:
    """Create a file with the specified content.

    Args:
        file_path (str): The full path where the file will be created containing the file name.
        content (str): The content to write into the file.

    Returns:
        str: A message indicating the file was created successfully.
    """
    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        with open(file_path, 'w') as file:
            file.write(content)
        
        return f"File created at {file_path}"
    except Exception as e:
        return f"Error creating file at {file_path}: {e}"
