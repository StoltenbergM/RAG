from langchain_community.document_loaders import TextLoader
from langchain_anthropic import 
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import CharacterTextSplitter
from langchain_chroma import Chroma

PATH = r"C:\Users\morte\Dropbox\Uni\Speciale\Litteratur"

# Load the document, split it into chunks, embed each chunk and load it into the vector store.
raw_documents = TextLoader(PATH).load()
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
documents = text_splitter.split_documents(raw_documents)
db = Chroma.from_documents(documents, OpenAIEmbeddings())