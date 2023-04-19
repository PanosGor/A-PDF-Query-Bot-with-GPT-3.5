from PyPDF2 import PdfReader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import ElasticVectorSearch, Pinecone, Weaviate, FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI
import os

class GPT_PDF():
    
    def __init__(self,pdf_path,API_Key):
        self.API_Key = API_Key
        self.reader = PdfReader(pdf_path)
        self.create_corpus()
        self.embedings()
        
    def create_corpus(self):
        os.environ["OPENAI_API_KEY"] = self.API_Key
        self.raw_text = ''
        for i, page in enumerate(self.reader.pages):
            text = page.extract_text()
            if text:
                self.raw_text += text
                
        #self.raw_text2 = raw_text.replace('\n',' ')
        
    def embedings(self):
        
        text_splitter = CharacterTextSplitter(        
                        separator = "\n",
                        chunk_size = 1000,
                        chunk_overlap  = 200,
                        length_function = len,
                    )
        self.texts = text_splitter.split_text(self.raw_text)
        self.embeddings = OpenAIEmbeddings()
        self.docsearch = FAISS.from_texts(self.texts, self.embeddings)
        self.chain = load_qa_chain(OpenAI(), chain_type="stuff")
        
        
    def query_corp(self,query):
        docs = self.docsearch.similarity_search(query)
        return self.chain.run(input_documents=docs, question=query)
                


        
        
        