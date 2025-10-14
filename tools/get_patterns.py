from langchain_core.tools import tool
from store.pgvector import vector_store

@tool
def get_patterns(pattern: str, language: str) -> str:
    """
    Retrieve code patterns or snippets based on a specified pattern and programming language.
    Examples: "repository structure in Clean Architecture", "Clean Architecture in Typescript".
    You should always call this tool when the user asks for code patterns or examples in a specific programming language.
    Useful for getting user's development patterns in a specific programming language.

    Args:
        pattern (str): The code pattern or snippet to search for.
        language (str): The programming language of the code pattern. Languages disponible: "TS", "GO".
    """
    try:
        results = vector_store.similarity_search(pattern, filter={"language": {"$eq": language.upper()}}, k=3)
        def _get_content(res):
            try:
                return res.metadata.get("content_text") or res.page_content
            except Exception:
                return res.page_content

        retorno = "\n\n".join([str(_get_content(result)) for result in results])
        print("Retorno get_patterns:", retorno)
        return retorno
    except Exception as e:
        return f"Error occurred: {e}"
