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

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a world class data scientist and RAG expert."),
    ("human", "Can you provide the code template for using RAG with langchain and with with the {model} model. The RAG should involve indexing, so it should embed my documents, and then probably embed the questions, and the relevant spltis should be retrived by the model, and then generate a response in the end. Please include a bit of description along the way")
])

response = prompt.invoke({"model": "anthropic"})
print(response.content)
'''
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

## Debugging
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
'''