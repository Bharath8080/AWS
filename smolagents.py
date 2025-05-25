from smolagents import LiteLLMModel, CodeAgent, DuckDuckGoSearchTool

# Your Sutra API Key
SUTRA_API_KEY = "........."

# Initialize Sutra model
model = LiteLLMModel(
    model_id="openai/sutra-v2",
    api_base="https://api.two.ai/v2",
    api_key=SUTRA_API_KEY,
    temperature=0.7,
    max_tokens=500
)

# Initialize CodeAgent with DuckDuckGo search tool and Sutra model
agent = CodeAgent(tools=[DuckDuckGoSearchTool()], model=model)

# Run a query using the agent
agent.run("ఐసీసీ 2025 ఫైనల్ ఎవరు గెలిచారు?")
