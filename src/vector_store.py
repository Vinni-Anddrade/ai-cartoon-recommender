from langchain_text_splitters import CharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_core.documents import Document
from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv
from src.configuration import Configuration
import pandas as pd


load_dotenv()


class VectorStoreBuilder:
    def __init__(self, data_path: str, persist_dir: str = "chroma_db"):
        self.data_path = data_path
        self.persist_dir = persist_dir

        config = Configuration()
        self.embedding = HuggingFaceEmbeddings(model_name=config.embedding_model_name)

        self.df = pd.read_csv(self.data_path, encoding="utf-8")

        self.build_documents()
        self.splitting_docs()
        self.embedding_texts()

    def build_documents(self):
        self.documents = list()
        for row in self.df.iterrows():
            id = row[0]
            page_content = row[1]["chunks"]

            doc = Document(
                page_content=page_content, metadata={"source": "df", "id": id}
            )

            self.documents.append(doc)

    def splitting_docs(self):
        splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
        self.texts_splitted = splitter.split_documents(self.documents)

    def embedding_texts(self):
        vector_store = Chroma.from_documents(
            self.texts_splitted,
            embedding=self.embedding,
            persist_directory=self.persist_dir,
        )
        vector_store.persist()

    def load_vector_store(self):
        return Chroma(
            persist_directory=self.persist_dir, embedding_function=self.embedding
        )
