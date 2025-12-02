from src.vector_store import VectorStoreBuilder
from src.recommender import CartoonRecommender
from src import Configuration
from src.utils.custom_exception import CustomException
from src.utils.logger import get_logger


logger = get_logger()


class CartoonRecomendationPipeline:
    def __init__(self, persist_dir: str = "chroma_db"):
        config = Configuration()

        try:
            logger.info("Initializing recommendation pipeline")
            vector_store_builder = VectorStoreBuilder(
                data_path="", persist_dir=persist_dir
            )

            retriever = vector_store_builder.load_vector_store().as_retriever()
            self.recommender = CartoonRecommender(
                retriever=retriever, model_name=config.llm_model_name
            )

            logger.info("Pipeline initialize sucessfully.")
        except Exception as e:
            logger.error(f"Failed to initialize pipeline {str(e)}")
            raise CustomException("Error during pipeline initialization", e)

    def recommend(self, question: str):
        try:
            logger.info(f"Recieved a query {question}")

            recomendation = self.recommender.recommendation_method(question)
            logger.info("Recommendation generated sucessfully.")
            return recomendation
        except Exception as e:
            logger.error(f"Failed to get the recommendation {str(e)}")
            raise CustomException("Error while getting the recommendation", e)
