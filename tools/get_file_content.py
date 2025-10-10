from langchain.tools import tool

@tool
def get_file_content(file_path: str) -> str:
    """Read and return the full content of a text file at the specified path.

    Opens the file in read mode and returns its entire content as a string. If the file
    does not exist, cannot be read, or an error occurs, returns an error message.
    Useful for inspecting source code, configuration files, or any readable text content.

    Args:
        file_path (str): The full path to the file to read.

    Returns:
        str: The file content as a string, or an error message if reading failed.
    """
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        return content
    except Exception as e:
        return f"Error reading file: {e}"