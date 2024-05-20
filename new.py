from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.chains.retrieval_qa import RetrievalQA
from langchain.llms import Anthropic
from key import ANTHROPIC_API_KEY

# Load your documents
loader = TextLoader(r"C:\Users\morte\Dropbox\Uni\Speciale\Litteratur")
documents = loader.load()

# Split the documents into smaller chunks
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
texts = text_splitter.split_documents(documents)

# Create a vector store to store the document embeddings
vectorstore = Chroma.from_documents(texts, embedding=None, persist_directory='path/to/persist/directory')

# Initialize the Anthropic LLM
llm = Anthropic(model='claude-v1', max_tokens=512)

# Create the Retrieval QA chain
qa = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=vectorstore.as_retriever(),
    return_source_documents=True,
)

# Ask a question
query = "What is the capital of France?"
result = qa({"query": query})

# Print the result
print(result['result'])
