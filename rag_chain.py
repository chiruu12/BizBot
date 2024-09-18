import os
from dotenv import load_dotenv
from langchain_cohere import CohereEmbeddings,ChatCohere
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains.retrieval import create_retrieval_chain
from langchain.prompts import PromptTemplate
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.retrievers import ContextualCompressionRetriever
from langchain_cohere import CohereRerank
from langchain_pinecone.vectorstores import PineconeVectorStore
from langchain_community.document_loaders import DirectoryLoader
from langchain_core.documents import Document
from pinecone import Pinecone
from langchain_community.document_loaders import TextLoader
from utils import pdf_to_text,extract_text_from_pdf
from langchain.globals import set_verbose

set_verbose(True) 

class RAG_Chain:
    def __init__(self):
        # Load environment variables
        load_dotenv()
        self.pinecone_api_key = os.getenv("PINECONE_API_KEY")
        self.cohere_api_key = os.getenv("COHERE_API_KEY")
        self.folder_path = os.getenv("FOLDER_PATH")
        self.index_name = os.getenv("PINECONE_INDEX_NAME")
        os.environ["COHERE_API_KEY"] = self.cohere_api_key
        
        # Initialize embeddings and vector store
        self.embeddings = CohereEmbeddings(cohere_api_key=self.cohere_api_key,model="embed-english-v3.0")
        pc = Pinecone(api_key=self.pinecone_api_key)
        self.index = pc.Index(self.index_name)
        self.vectorstore = PineconeVectorStore(index = self.index, pinecone_api_key = self.pinecone_api_key,embedding = self.embeddings)

        self.update_vectorstore_with_files()
        # Initialize LLM and components for RAG chain
        self.llm = ChatCohere(model='command-r')
        self.template = """You are a helpful AI assistant. Use the following context to answer the user's question. If you don't know the answer, just say that you don't know, don't try to make up an answer.
        you will be given data related to company and u will answer the questions using those details
        Context: {context}
        Query: {input}
        Answer:"""
        self.prompt = PromptTemplate.from_template(self.template)
        self.reranker = CohereRerank(model='rerank-english-v3.0')
        self.compression_retriever = ContextualCompressionRetriever(
            base_retriever=self.vectorstore.as_retriever(),
            base_compressor = self.reranker
        )
        question_answer_chain = create_stuff_documents_chain(
            llm=self.llm,
            prompt=self.prompt
        )
        self.chain = create_retrieval_chain(
            retriever=self.compression_retriever,
            combine_docs_chain= question_answer_chain
        )
        
    def update_vectorstore_with_files(self,file=None):
        """Update the vector store with the PDFs uploaded by the user"""
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
        if file:
            text = pdf_to_text(file)
            text_chunks = text_splitter.split_text(text)
            documents = [Document(page_content=chunk) for chunk in text_chunks]
            if not documents:
                return
            self.vectorstore.add_documents(documents=documents)
        else:
            text_loader_kwargs = {"autodetect_encoding": True}
            loader = DirectoryLoader(path = self.folder_path,loader_cls=TextLoader,loader_kwargs=text_loader_kwargs)
            directory = loader.load()
            documents = []
            for file in directory:
                file_path = file.metadata.get('source')
                text=extract_text_from_pdf(file_path)
                splits = text_splitter.split_text(text)  # Splits text into chunks
                text_chunks = [Document(page_content=chunk) for chunk in splits]
                documents.extend(text_chunks)
                
            self.vectorstore.add_documents(documents=documents)
                
    def get_rag_chain(self):
        """Return the RAG chain."""
        return self.chain