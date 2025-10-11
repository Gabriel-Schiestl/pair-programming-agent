from langchain_core.tools import tool
from store.pgvector import vector_store

@tool
def get_patterns(pattern: str, language: str) -> str:
    """
    Retrieve code patterns or snippets based on a specified pattern and programming language.
    Examples: "repository structure in Clean Architecture", "Clean Architecture in Typescript".
    Useful for getting user's development patterns in a specific programming language.

    Args:
        pattern (str): The code pattern or snippet to search for.
        language (str): The programming language of the code pattern.
    """
    try:
        results = vector_store.similarity_search(pattern, filter={"language": language}, k=3)
        return "\n\n".join([str(result.page_content) for result in results])
    except Exception as e:
        return f"Error occurred: {e}"
