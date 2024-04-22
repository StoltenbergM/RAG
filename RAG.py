from langchain_anthropic import ChatAnthropic
from langchain_core.prompts import ChatPromptTemplate
from key import ANTHROPIC_API_KEY

# https://www.freecodecamp.org/news/beginners-guide-to-langchain/

ANTHROPIC_API_KEY=ANTHROPIC_API_KEY

chat_model = ChatAnthropic(
    model="claude-3-sonnet-20240229",
    temperature=0,
    api_key=ANTHROPIC_API_KEY
)

chat_model.invoke("Tell me a joke about bears!")

joke_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a world class comedian."),
    ("human", "Tell me a joke about {topic}")
])

joke_prompt.invoke({"topic": "beets"})