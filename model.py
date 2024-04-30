from langchain_anthropic import ChatAnthropic
from key import ANTHROPIC_API_KEY
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import database_processing
import os
from os import path
import sys

''' --------------------------------------- Model used -----------------------------------------'''
ANTHROPIC_API_KEY=ANTHROPIC_API_KEY
chat_model = ChatAnthropic(
    model="claude-3-sonnet-20240229",
    temperature=0,
    api_key=ANTHROPIC_API_KEY
)

''' ------------------------------- Input data - Choice of data ---------------------------------'''
# Which type of documents to use
word2txt = True
pdf2txt = True

# New folder name for .txt data-folder
data_folder_name = "RAG data"

# Set the path to the folder containing your text files
folder_path = r"C:\Users\morte\Dropbox\Uni\Speciale\Litteratur\Om Hydrogen"

''' ------------------------------- Input data - Choice of data ---------------------------------'''

if not path.exists(folder_path):
    print("\nFile name or path could not be found\nCheck pathname and try again..")
    sys.exit()

# create .txt file for all word files - from datatransform
path_data = database_processing.File2txt(folder_path, data_folder_name, word2txt, pdf2txt)

# Checking size of the new folder
folder_size = 0
nu_of_files = 0
for root, dirs, files in os.walk(path_data):
    for file in files:
        folder_size += os.path.getsize(os.path.join(root, file))
        nu_of_files += 1

proceed = input(f'\nThe data-folder "{data_folder_name}" consists of {nu_of_files} file(s) with an accumulative '
                f'size of {int(folder_size / 1000)} KB. \nDo you want to proceed and train the model? (y/n): ')
if proceed.lower() != "y":
    print("Exiting the script...")
    exit()

# Load text files as a list of strings
data_files = []
for file in os.listdir(path_data):
    if file.endswith(".txt"):
        with open(os.path.join(path_data, file), "r", encoding="utf-8") as f:
            data_files.append(f.read())

# Create a Dataset object from the loaded text files
SOURCE = data_files
print(f"Type of data: {type(SOURCE)}")
''' ---------------------------------------------------------------------------------------------------- '''

rag_prompt = ChatPromptTemplate.from_messages([
    ("system", 'You are a helpful assistant. Use the following context when responding:\n\n{context}.'),
    ("human", "{question}")
])

rag_chain = rag_prompt | chat_model | StrOutputParser()

response = rag_chain.invoke({
    "question": "How much Hydrogen did the U.S. produce? Please note where you found the answer in the provided context",
    "context": SOURCE
})

print(response)