# from prompts import research_agent_prompt
from langchain.agents import create_agent
from langchain.agents.middleware import SummarizationMiddleware
from prompts import research_agent_prompt
from tools import internet_search
from models import sub_agent_llm

# Research Sub Agent Description
research_sub_agent_description = """Expert business intelligence researcher. Conducts deep-dive research on companies, products, pricing, and markets. Give focused queries on specific topics - for multiple topics, call multiple agents in parallel using the task tool."""

# Define Middleware
research_sub_agent_middleware = [
    SummarizationMiddleware(
        model=sub_agent_llm,
        max_tokens_before_summary=120000,
        messages_to_keep=20,
    ),
]

# Define the Research Sub Agent Graph
research_sub_agent_graph = create_agent(
    model=sub_agent_llm,
    tools=[internet_search],
    prompt=research_agent_prompt,   
    middleware=research_sub_agent_middleware,
        ).with_config({"recursion_limit": 1000}) # Using a custom graph to pass a longer recursion limit

# Define the Research Sub Agent
research_sub_agent = {
    "name": "research-agent",
    "description": research_sub_agent_description,
    "graph": research_sub_agent_graph
}