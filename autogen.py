from autogen import ConversableAgent, UserProxyAgent

# LiteLLM server config for Sutra model (adjust API key and base_url as needed)
local_llm_config = {
    "config_list": [
        {
            "model": "sutra-v2",                # Correct model ID for Sutra
            "api_key": "..........",  # Your Sutra API key
            "base_url": "https://api.two.ai/v2",  # Sutra API base URL
            "price": [0, 0],                    # Pricing (0 for dev/testing)
        }
    ],
    "cache_seed": None  # Disable caching for fresh results
}

assistant = ConversableAgent("assistant", llm_config=local_llm_config)
user_proxy = UserProxyAgent("user", code_execution_config=False)

# Start chat and get the assistant's direct reply to a user message
response = assistant.initiate_chat(user_proxy, message="How can I help you today?")

# Print only the assistant's reply text directly
print(response.message.content)
