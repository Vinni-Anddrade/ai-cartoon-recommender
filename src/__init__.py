from src.utils.utils import read_yaml


class Configuration:
    def __init__(self):
        self.config_path = "./src/config/config.yml"

        config = read_yaml(self.config_path)
        self.llm_model_name = config.LLM_MODEL_NAME
        self.embedding_model_name = config.EMBEDDING_MODEL_NAME
