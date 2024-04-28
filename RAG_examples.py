from langchain_anthropic import ChatAnthropic
from key import ANTHROPIC_API_KEY
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

ANTHROPIC_API_KEY=ANTHROPIC_API_KEY

chat_model = ChatAnthropic(
    model="claude-3-sonnet-20240229",
    temperature=0,
    api_key=ANTHROPIC_API_KEY
)

SOURCE = """
Old Ship Saloon 2023 quarterly revenue numbers:
Q1: $174782.38
Q2: $467372.38
Q3: $474773.38
Q4: $389289.23
"""

rag_prompt = ChatPromptTemplate.from_messages([
    ("system", 'You are a helpful assistant. Use the following context when responding:\n\n{context}.'),
    ("human", "{question}")
])

rag_chain = rag_prompt | chat_model | StrOutputParser()

response = rag_chain.invoke({
    "question": "What was the Old Ship Saloon's total revenue in Q1 2023?",
    "context": SOURCE
})

print(response)