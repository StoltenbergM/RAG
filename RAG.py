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

joke_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a world class comedian."),
    ("human", "Tell me a joke about {topic}")
])

## Chaining
chain = joke_prompt | chat_model

## Output Parser (Making the output a string)
from langchain_core.output_parsers import StrOutputParser

str_chain = chain | StrOutputParser()

# Equivalent to:
# str_chain = joke_prompt | chat_model | StrOutputParser()
#response = str_chain.invoke({"topic": "beets"})

## Streaming (Will yield output faster, cut them into chunks)

#for chunk in str_chain.stream({"topic": "beets"}):
    #print(chunk, end="|")

## Context (The core of RAG)
from langchain.globals import set_debug

set_debug(True)

from datetime import date

prompt = ChatPromptTemplate.from_messages([
    ("system", 'You know that the current date is "{current_date}".'),
    ("human", "{question}")
])

chain = prompt | chat_model | StrOutputParser()

response = chain.invoke({
    "question": "What is the current date?",
    "current_date": date.today()
})

print(response)