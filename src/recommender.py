from langchain.chains.retrieval_qa.base import RetrievalQA
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from src.prompt_template import cartoon_prompt


load_dotenv()


class CartoonRecommender:
    def __init__(self, retriever, model_name: str):
        self.retriever_ = retriever
        self.model_name_ = model_name

        self.llm_model = ChatGroq(model=self.model_name_, temperature=0)
        self.prompt = cartoon_prompt()

        self.qa_chain = RetrievalQA.from_chain_type(
            llm=self.llm_model,
            chain_type="stuff",
            retriever=self.retriever_,
            return_source_documents=True,
            chain_type_kwargs={"prompt": self.prompt},
        )

    def recommendation_method(self, question: str):
        result = self.qa_chain(inputs={"query": question})
        return result["result"]
