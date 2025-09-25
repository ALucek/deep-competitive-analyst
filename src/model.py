from langchain_openai import ChatOpenAI

agent_llm = ChatOpenAI(model="gpt-5-2025-08-07")
sub_agent_llm = ChatOpenAI(model="gpt-5-mini-2025-08-07")