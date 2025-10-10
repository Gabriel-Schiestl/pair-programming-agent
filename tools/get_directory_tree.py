from langchain.tools import tool
import os

@tool
def get_directory_tree(path: str) -> str:
    """Generate a visual tree representation of the directory structure at the specified path.

    Recursively lists all files and subdirectories in a tree format using Unicode connectors.
    Entries are sorted alphabetically for consistent output. Returns an error message if the
    path does not exist or is not a directory. Useful for exploring and documenting project structures.

    Args:
        path (str): The full path to the directory to analyze.

    Returns:
        str: A multi-line string representing the directory tree, or an error message.
    """

    def tree(dir_path, prefix=""):
        entries = sorted(os.listdir(dir_path))
        entries_count = len(entries)
        for index, entry in enumerate(entries):
            entry_path = os.path.join(dir_path, entry)
            connector = "└── " if index == entries_count - 1 else "├── "
            yield prefix + connector + entry
            if os.path.isdir(entry_path):
                extension = "    " if index == entries_count - 1 else "│   "
                yield from tree(entry_path, prefix + extension)

    try:
        if not os.path.exists(path):
            return f"Path does not exist: {path}"
        if not os.path.isdir(path):
            return f"Path is not a directory: {path}"
        return "\n".join(tree(path))
    except Exception as e:
        return f"Error retrieving directory tree: {e}"