from dotenv import load_dotenv

from src.data_loader import CartoonDataLoader
from src.vector_store import VectorStoreBuilder
from src.utils.custom_exception import CustomException
from src.utils.logger import get_logger


load_dotenv()
logger = get_logger(__name__)


def main():
    try:
        logger.info("Starting to build pipeline.")
        loader = CartoonDataLoader(
            "./src/data/anime_with_synopsis.csv",
            "./src/data/cartoon_processed.csv",
        )
        processed_csv_path = loader.loading_and_processing()
        logger.info("The data was loaded and processed")

        breakpoint()
        _ = VectorStoreBuilder(processed_csv_path).load_vector_store()
        logger.info("Vector Store built sucessfully")

        logger.info("Pipeline built sucessfully")

    except Exception as e:
        logger.error(f"Failed to execute pipeline {str(e)}")
        raise CustomException("Error while creating the pipeline", e)


if __name__ == "__main__":
    main()
