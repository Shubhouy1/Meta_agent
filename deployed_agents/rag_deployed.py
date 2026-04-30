import os
from typing import List

# Langchain Core
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableParallel, RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

# Langchain Google GenAI
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings

# Langchain Chroma
from langchain_chroma import Chroma

# Langchain Community Loaders
from langchain_community.document_loaders import PyPDFLoader

# Langchain Text Splitters
from langchain_text_splitters import RecursiveCharacterTextSplitter


class Agent:
    """
    A RAG agent for answering questions from PDF documents using ChromaDB and Google Generative AI.
    """

    def __init__(self):
        try:
            # Ensure GOOGLE_API_KEY is set in environment variables
            if not os.getenv("GOOGLE_API_KEY"):
                raise ValueError(
                    "GOOGLE_API_KEY environment variable not set. "
                    "Please set it before running the agent."
                )

            # Initialize embedding model
            self.embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")

            # Initialize ChromaDB vector store
            # It will create a persistent collection named "pdf_qa_collection"
            # If it exists, it will load it.
            self.vectorstore = Chroma(
                collection_name="pdf_qa_collection", embedding_function=self.embeddings
            )

            # Initialize the Generative AI model
            self.llm = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0.3)

            # Define the RAG prompt template
            self.prompt = ChatPromptTemplate.from_template(
                """You are an AI assistant for answering questions about documents.
                Use the following pieces of retrieved context to answer the question.
                If you don't know the answer, just say that you don't know.
                Use three sentences maximum and keep the answer concise.

                Question: {question}
                Context: {context}
                Answer:"""
            )

            # Construct the RAG chain
            self.rag_chain = (
                RunnableParallel(
                    {"context": self.vectorstore.as_retriever(), "question": RunnablePassthrough()}
                )
                | self.prompt
                | self.llm
                | StrOutputParser()
            )
            print("Agent initialized successfully.")

        except ValueError as e:
            print(f"Initialization Error: {e}")
            raise
        except Exception as e:
            print(f"An unexpected error occurred during agent initialization: {e}")
            raise

    def load_documents(self, pdf_paths: List[str]):
        """
        Loads PDF documents, splits them into chunks, and adds them to the vector store.
        """
        all_docs = []
        try:
            for pdf_path in pdf_paths:
                if not os.path.exists(pdf_path):
                    print(f"Warning: PDF file not found at {pdf_path}. Skipping.")
                    continue
                print(f"Loading documents from {pdf_path}...")
                loader = PyPDFLoader(pdf_path)
                docs = loader.load()
                all_docs.extend(docs)

            if not all_docs:
                print("No documents were loaded. Vector store remains unchanged.")
                return

            # Split documents into smaller chunks
            text_splitter = RecursiveCharacterTextSplitter(
                chunk_size=1000, chunk_overlap=200
            )
            splits = text_splitter.split_documents(all_docs)
            print(f"Split {len(all_docs)} documents into {len(splits)} chunks.")

            # Add documents to the vector store
            print("Adding document chunks to ChromaDB...")
            self.vectorstore.add_documents(splits)
            print("Documents successfully added to ChromaDB.")

        except Exception as e:
            print(f"Error loading or processing documents: {e}")

    def run(self, user_input: str) -> str:
        """
        Runs the RAG chain to answer a question based on the loaded documents.
        """
        try:
            if not user_input.strip():
                return "Please provide a non-empty question."

            print(f"\nUser question: {user_input}")
            response = self.rag_chain.invoke(user_input)
            return response
        except Exception as e:
            return f"An error occurred while processing your question: {e}"


if __name__ == "__main__":
    # Create a dummy PDF for testing if it doesn't exist
    # In a real scenario, users would upload their own PDFs.
    dummy_pdf_content = """
    # Sample Document for PDF QA System

    ## Introduction
    This is a sample PDF document created to test the PDF QA system. It contains various pieces of information that can be queried.

    ## Section 1: Project Overview
    The project aims to develop an intelligent agent capable of answering questions from uploaded PDF documents. It leverages vector search for efficient retrieval of relevant information. The primary technologies used include Google Generative AI for language understanding and generation, and ChromaDB for vector storage and retrieval.

    ## Section 2: Key Features
    1.  **Document Upload**: Users can upload multiple PDF files.
    2.  **Vector Search**: Documents are processed, embedded, and stored in a vector database (ChromaDB).
    3.  **Question Answering**: The agent can answer natural language questions based on the content of the uploaded documents.
    4.  **Scalability**: Designed to handle small to medium datasets efficiently.

    ## Section 3: Technical Details
    The system uses `langchain_google_genai` for the LLM and embeddings, and `langchain_chroma` for the vector store. Document loading is handled by `langchain_community.document_loaders.PyPDFLoader`, and text splitting by `langchain_text_splitters.RecursiveCharacterTextSplitter`. The agent orchestrates these components using LangChain's Runnable interface.

    ## Conclusion
    This system provides a robust framework for building PDF-based question-answering applications.
    """
    dummy_pdf_path = "sample_document.pdf"

    try:
        from reportlab.pdfgen import canvas
        from reportlab.lib.pagesizes import letter

        if not os.path.exists(dummy_pdf_path):
            print(f"Creating dummy PDF: {dummy_pdf_path}")
            c = canvas.Canvas(dummy_pdf_path, pagesize=letter)
            textobject = c.beginText()
            textobject.setTextOrigin(50, 750)
            textobject.setFont("Helvetica", 12)
            for line in dummy_pdf_content.split('\n'):
                textobject.textLine(line)
            c.drawText(textobject)
            c.save()
            print("Dummy PDF created.")
        else:
            print(f"Dummy PDF '{dummy_pdf_path}' already exists.")

    except ImportError:
        print("reportlab not installed. Cannot create dummy PDF.")
        print("Please install it (`pip install reportlab`) or manually place a PDF at 'sample_document.pdf'.")
        print("Skipping dummy PDF creation.")
    except Exception as e:
        print(f"Error creating dummy PDF: {e}")


    agent = None
    try:
        agent = Agent()
    except Exception as e:
        print(f"Failed to initialize agent. Exiting. Error: {e}")
        exit(1)

    # Load documents into the agent's vector store
    # Replace with your actual PDF paths
    if os.path.exists(dummy_pdf_path):
        agent.load_documents([dummy_pdf_path])
    else:
        print("No PDF documents loaded. Please ensure 'sample_document.pdf' exists or provide other paths.")

    print("\n--- PDF QA System Ready ---")
    print("Ask questions about the loaded documents. Type 'exit' to quit.")

    while True:
        question = input("\nYour question: ")
        if question.lower() == "exit":
            print("Exiting QA system. Goodbye!")
            break

        if agent:
            answer = agent.run(question)
            print(f"Agent's Answer: {answer}")
        else:
            print("Agent not initialized. Cannot answer questions.")
            break