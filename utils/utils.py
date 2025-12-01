from box import ConfigBox
import yaml


def read_yaml(path: str):
    with open(path, "r") as yaml_file:
        yaml_ = yaml.safe_load(yaml_file)
        return ConfigBox(yaml_)
