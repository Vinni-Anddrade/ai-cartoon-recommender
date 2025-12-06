from langchain_groq import ChatGroq
from dotenv import load_dotenv
from src.prompt_template import cartoon_prompt
from langchain_community.vectorstores import Chroma


load_dotenv()


class CartoonRecommender:
    def __init__(self, retriever: Chroma, model_name: str):
        self.retriever_ = retriever
        self.model_name_ = model_name

        self.llm_model = ChatGroq(model=self.model_name_, temperature=0)
        self.prompt = cartoon_prompt()

    def recommendation_method(self, question: str):
        self.response_vector_ = self.retriever_.similarity_search(query=question, k=3)

        self.response_documents = " || ".join([i.page_content for i in self.response_vector_])
        breakpoint()
        chain = self.prompt | self.llm_model
        result = chain.invoke(
            input={"question": question, "context": self.response_documents}
        ).content

        return result
