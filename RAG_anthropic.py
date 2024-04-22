from langchain_anthropic import ChatAnthropic
from key import ANTHROPIC_API_KEY

ANTHROPIC_API_KEY=ANTHROPIC_API_KEY

chat_model = ChatAnthropic(
    model="claude-3-sonnet-20240229",
    temperature=0,
    api_key=ANTHROPIC_API_KEY
)

chat_model.invoke("Tell me a joke about bears!")