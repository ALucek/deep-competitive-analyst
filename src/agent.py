from deepagents import create_deep_agent
from model import agent_llm
from sub_agent import research_sub_agent
from prompts import competitive_analysis_prompt
from tools import internet_search

# Compile the deep agent
competitive_analysis_agent = create_deep_agent(
    tools = [internet_search],
    instructions = competitive_analysis_prompt,
    subagents = [research_sub_agent],
    model = agent_llm
).with_config({"recursion_limit": 1000})