from perplexity import Perplexity
import perplexity

# Initialize the Perplexity client
perplexity_client = Perplexity()

# Define the internet search tool
def internet_search(
        query: str, 
    ) -> str:  
    """
    Internet search tool able to provide detailed search results and page content.

    Args:
        query: The search query to perform.
    
    Returns:
        A string containing the top search results and page content.
    """

    try:
        search_results = perplexity_client.search.create(
            query=query,
            max_results=5,
            max_tokens_per_page=2048,
            max_tokens=24576,
        )
    
    except perplexity.BadRequestError as e:
        return f"Invalid search parameters: {e}"
    except perplexity.RateLimitError as e:
        return "Search rate limit exceeded"
    except perplexity.APIStatusError as e:
        return f"Search API error {e.status_code}: {e}"
    except Exception as e:
        return f"Unexpected error: {e}"
    
    return search_results.results