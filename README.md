# Deep Competitive Analyst

<img src="./dca_logo.png" width=200>

Deep Competitive Analyst is a 'deep agent' style LLM assistant built to automate the creation of company profiles and competitive analyses. Built on top of [deepagents](https://github.com/langchain-ai/deepagents), [LangGraph Platform](https://www.langchain.com/langgraph-platform), and [Perplexity Search](https://docs.perplexity.ai/getting-started/overview), DCA can perform thorough research autonomously to create detailed business reports in a fraction of the time of a human. It operates for extended periods, dynamically spawning sub-agents to parallelize research tasks and creates the kind of in-depth competitive analysis that usually costs thousands.

Example output from the agent [can be viewed here.](./example_output/)

## Installation

1. Clone the repository:

```bash
git clone https://github.com/ALucek/deep-competitive-analyst.git
cd deep-competitive-analyst
```

2. Install depencies:

```bash
uv sync
```

3. Create a .env file with the following variables:

```env
OPENAI_API_KEY=<your-api-key>
PERPLEXITY_API_KEY=<your-api-key>
LANGSMITH_API_KEY=<your-api-key>
LANGSMITH_TRACING=true
LANGSMITH_ENDPOINT=https://api.smith.langchain.com
LANGSMITH_PROJECT=deep_competitive_analyst
```

3. Launch the agent:

```bash
cd src
uv run langgraph dev  
```

The Deep Competitive Analyst will now be running locally via the langgraph platform and can be integrated into your own compatible interface. It is recommended to use LangSmith Studio for local testing.

## Contributing

Contributions welcome! Feel free to submit a PR

Todo List:  
- Dedicated front end
- File saving outside of state
- Better filtering KWARGS for search tool
- Test performance with different/smaller models
- Human in the loop tool for clarifications from main system
- Kickoff scope clarification
- Conversation reconstruction from sub agent context for followup QnA
- Better middleware management
- Better company profile formatting

## License

Apache-2.0 License - See [LICENSE](LICENSE)

[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
