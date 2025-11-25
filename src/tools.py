from perplexity import Perplexity
import perplexity
from ratelimit import limits, sleep_and_retry

# Initialize the Perplexity client
perplexity_client = Perplexity()

# Define the internet search tool
@sleep_and_retry
@limits(calls=3, period=1) # Rate limited to 3 req/sec for Perplexity API
def internet_search(query: str) -> str:  
    """
    Internet search tool able to provide detailed search results and page content.

    Search queries should follow these guidelines:
    1. Use natural language queries — Write searches as complete, descriptive phrases rather than fragmented keywords. For example, use "latest developments in quantum computing error correction 2024" instead of "quantum computing news -ads site:arxiv.org".
    2. Be specific in a single query — Include all relevant context (topic, timeframe, domain) directly in your search phrase. For example, "OpenAI GPT-5 announcement features March 2025" rather than running multiple searches.
    3. Avoid search engine operators — Do not use syntax like `site:`, `filetype:`, `-`, `OR`, or quotation marks for exact matching. The API handles relevance internally and these operators often degrade results.
    4. One clear intent per search — Each query should answer one specific question. Instead of "AI regulations EU and US comparison pros cons," split into focused searches like "European Union AI Act key requirements 2024" and "United States federal AI regulation policies 2024".

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