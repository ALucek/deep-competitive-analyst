# from langchain_core.tools import tool
from tavily import TavilyClient
from typing import Literal
import os

tavily_client = TavilyClient(api_key=os.environ["TAVILY_API_KEY"])

# Define web search tool
# @tool
def internet_search(
    query: str,
    max_results: int = 5,
    topic: Literal["general", "news", "finance"] = "general",
    include_raw_content: bool = False,
):
    """Run a web search"""
    search_docs = tavily_client.search(
        query,
        max_results=max_results,
        include_raw_content=include_raw_content,
        topic=topic,
    )
    return search_docs