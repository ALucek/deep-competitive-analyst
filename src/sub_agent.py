from prompts import research_agent_prompt
from tools import internet_search
from model import sub_agent_llm

# Research Sub Agent
research_sub_agent_description = """Expert business intelligence researcher. Use for deep-dive research on specific aspects of companies (e.g., 'Company A pricing and packaging details', 'Company B customer reviews and satisfaction', 'recent partnerships and acquisitions for Company A'). Always call with ONE focused research topic. For multiple topics, call multiple times in parallel."""

research_sub_agent = {
    "name": "research-agent",
    "description": research_sub_agent_description,
    "prompt": research_agent_prompt,
    "model": sub_agent_llm,
    "tools": [internet_search],
}