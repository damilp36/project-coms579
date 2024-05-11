# Retrieveal Augumented Generation (RAG)

Retrieval-Augmented Generation for Question-Answering on PDFs

## Link to Youtube Video
- Milestone 1: https://youtu.be/mkO-TYDTxWk 
- Milestone 2: https://youtu.be/Q8WnpHwXv9I 
- Milestone 3: https://youtu.be/v1vRKPnkI3h

## Overview
This project provides a Retrieval-Augmented Generation (RAG) based solution for extracting answers from PDF documents. It Leverages LangChain for document processing and answer generation pipelines, LangChain Vectors for embedding, and Streamlit for the user interface.

## Language
- Python 3

## Dependencies 
- python-dotenv [Documentation](https://pypi.org/project/python-dotenv/)
- PyPDF2  [Documentation](https://pypdf2.readthedocs.io/)
- pypdf  [Documentation](https://pypdf.readthedocs.io/en/latest/)
- Faiss CPU [Documentation](https://faiss.ai/index.html)
- langchain-openai faiss-cpu  [Documentation](https://python.langchain.com/docs/integrations/vectorstores/faiss)
- Lang-chain [Documentation](https://python.langchain.com/docs)
- LanG-Chain OPENAI [Documentation](https://python.langchain.com/docs/integrations/llms/openai/)
- StreamIt [Documentation](https://docs.streamlit.io/)

## How to Install
- Install all the dependencies:
    ```
    %pip install -r requirements.txt
    ```

- Alternatively, install the packages you need:
    - PyPDF2
        ```
        %pip install pypdf2
        ```
    - pypdf 
        ```
        %pip install pypdf
        ```
    - Python dotenv
        ```
        %pip install python-dotenv
        ```
    - Faiss CPU
        ```
        pip install faiss-cpu  
        ```
    - Lang chain OpenAI Faiss CPU
        ```
        pip install --upgrade langchain-openai faiss-cpu  
        ```
    - Langchain 
        ```
        %pip install langchain
        ```
    - Langchain-openAI
        ```
        %pip install langchain-openai
        ```

## Functions 
- PDF Upload and Indexing
- PDF Deletion
- Vector-Based Retrieval
- Question Answering

## Set up Environment
1. Create a .env file.
2. Add the following fields:
    - OPENAI_API_KEY = 'your_api_key'
    - LANG_CHAIN_API_KEY = 'your_api_key'
3. Add the .env file to your gitignore.

## Usage Examples

### Run all commands from CLI with Python integrated

#### A. PDF Operations
1. `list.py`: Returns a list of all uploaded PDFs.
   - Usage: `python3 list.py`
   - Response:
        - On success: Returns a list of PDF files and the count.
        - On failure: Error: No PDF files present.

2. `upload.py`: Uploads a PDF to the document directory.
   - Usage: `python3 upload.py --pdf_file=sample.pdf`
   - Response:
        - On success: 
            ```
            Upload successful! 
            Uploaded path and filename: document/file_sample.pdf
            ```
        - On failure: [Errno 2] No such file or directory.

3. `retrieve.py`: Retrieves a PDF by name along with its content.
   - Usage: `python3 retrieve.py --pdf_file=sample.pdf`
   - Response:
        - On success: `{'filename': 'sample.pdf', 'content': "lifelong"}`
        - On failure: Error: PDF file 'sample.pdf' not found in 'document'.

4. `delete.py`: Deletes a PDF by name and returns the current directory count.
   - Usage: `python3 delete.py --pdf_file=sample.pdf`
   - Response:
        - On success: `{'filename': 'sample.pdf', 'content': "lifelong"}`
        - On failure: 
            ```
            PDF count before deletion: 2
            PDF count after deletion: 1
            sample.pdf deleted successfully.
            ```

5. `query.py`: Queries a PDF and returns an answer with a character limit of 300.
   - Usage: `python3 query.py --question="What are heat exchangers?"`
   - Response:
        - On success: `{'page_number': 'answer'}`
        - On failure: An error has occurred.
