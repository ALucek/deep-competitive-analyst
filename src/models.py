from langchain_openai import ChatOpenAI

# Define the agent and sub agent models
agent_llm = ChatOpenAI(model="gpt-5.1-2025-11-13", max_retries=3)
sub_agent_llm = ChatOpenAI(model="gpt-5.1-2025-11-13", max_retries=3)