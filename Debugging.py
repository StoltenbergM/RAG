from langchain_anthropic import ChatAnthropic
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from key import ANTHROPIC_API_KEY

# https://www.freecodecamp.org/news/beginners-guide-to-langchain/

ANTHROPIC_API_KEY = ANTHROPIC_API_KEY

chat_model = ChatAnthropic(
    model="claude-3-sonnet-20240229",
    temperature=0,
    api_key=ANTHROPIC_API_KEY
)

## Debugging
from langchain.globals import set_debug

from datetime import date

prompt = ChatPromptTemplate.from_messages([
    ("system", 'You know that the current date is "{current_date}".'),
    ("human", "{question}")
])

chain = prompt | chat_model | StrOutputParser()
## simpel debug:

## Can turn debug mode of or on for more info or clarity
set_debug(True)

response = chain.invoke({
    "question": "What is the current date?",
    "current_date": date.today()
})

print(response)
'''
set_debug(False)

# Define an asynchronous function to run the code
import asyncio
async def main():
    # Invoke the chain and stream events
    stream = chain.astream_events({
        "question": "What is the current date?",
        "current_date": date.today()
    }, version="v1")

    async for event in stream:
        print(event)
        print("-----")

# Run the asynchronous function
asyncio.run(main())
'''