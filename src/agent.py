from deepagents import create_deep_agent
from models import agent_llm
from sub_agents import research_sub_agent
from prompts import competitive_analysis_prompt

# Compile the Competitive Analysis Agent
competitive_analysis_agent = create_deep_agent(
    system_prompt = competitive_analysis_prompt,
    subagents = [research_sub_agent],
    model = agent_llm
).with_config({"recursion_limit": 1000})