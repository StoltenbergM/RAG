import os
import docx2txt
import PyPDF2
from PyPDF2 import PdfReader, PdfWriter
from datetime import datetime

# Iterate over all files in the folder with a .docx extension
def File2txt(folder_path, data_folder_name, word2txt=True, pdf2txt=True):
    """
    :param folder_path: The path to the folder that should be used for the dataset
    :param data_folder_name: Name of the new folder that stores the text-data
    :param word2txt: Boolean determining if docx-files should be used for the dataset
    :param pdf2txt: Boolean determining if pdf-files should be used for the dataset
    """
    # Create a new folder for all the .txt data in the parent folder
    new_folder_path = os.path.join(folder_path, data_folder_name)
    # Check for existing folder
    if os.path.exists(new_folder_path):
        # Using existing data
        existing_file = input(f"'{data_folder_name}' folder already exists in {folder_path}. "
                        f"\nDo you want to use the existing file for the model? (y/n): ")
        if existing_file.lower() == "y":
            print(f"Using existing dataset in {data_folder_name}...")
            return new_folder_path
        else:
            proceed = input(f'\nDo you still want to proceed? (y/n): ')
            if proceed.lower() != "y":
                print("Exiting the script...")
                exit()
    else:
        os.makedirs(new_folder_path)

    conversion_counter = 0

    # walk through all folders and subfolder from the path
    for foldername, subfolders, filenames in os.walk(folder_path):
        for filename in filenames:
            if word2txt and filename.endswith(".docx"):
                conversion_counter += 1
                # Get the full path of the docx file
                filepath = os.path.join(foldername, filename)

                # Convert the docx file to text
                text = docx2txt.process(filepath)

            elif pdf2txt and filename.endswith(".pdf"):
                conversion_counter += 1
                # Get the full path of the pdf file
                filepath = os.path.join(foldername, filename)

                # Convert the pdf file to text
                with open(filepath, 'rb') as pdf_file:
                    pdf_reader = PyPDF2.PdfReader(pdf_file)
                    text = ""
                    for page in range(len(pdf_reader.pages)):
                        page_obj = pdf_reader.pages[page]
                        text += page_obj.extract_text()

            # continue to next iteration if no pdf or docx can be converted
            else:
                continue

            # Get parent folder name
            parent_folder_name = os.path.basename(os.path.abspath(folder_path))

            # Get folder and subfolder names
            folder_names = os.path.relpath(foldername, folder_path).split(os.path.sep)

            # ____________________________________________________________________________________________________
            # Information to each .txt file
            header = ""

            header += "Information about the file:\nThis document was found in the following folder(s):\n"

            # Construct the header based on the folder and sub-folder name
            if parent_folder_name:
                header += f"Parent folder: {parent_folder_name}\n"
            for i, folder_name in enumerate(folder_names):
                header += f"Sub{'sub'*i}folder: {folder_name}\n"

            # Get file creation and modification time
            ctime = os.path.getctime(filepath)
            mtime = os.path.getmtime(filepath)
            creation_time = datetime.fromtimestamp(ctime).strftime('%Y-%m-%d %H:%M:%S')
            modification_time = datetime.fromtimestamp(mtime).strftime('%Y-%m-%d %H:%M:%S')

            # Add creation and modification time to header
            header += "Timestamps of relevant information for this document:\n"
            header += f"Time of creation: {creation_time}\n"
            header += f"Time of last modification: {modification_time}\n\n"

            text = header + text
            # ____________________________________________________________________________________________________

            # Create text file name with folder names
            text_filename = filename[:-5] + ".txt"

            # Save text file in new folder
            text_path = os.path.join(new_folder_path, text_filename)

            # Save the text inside the new text file
            with open(text_path, "w", encoding="utf-8") as text_file:
                text_file.write(text)

            print(f"Converted '{filename}' from {parent_folder_name}")

    if conversion_counter == 0:
        print(f"There was no .docx files located in the choosen folder")
    elif conversion_counter > 1:
        print(f"\n --- Succesfully converted {conversion_counter} files to text-format ---")

    return new_folder_path
