from setuptools import setup, find_packages


with open("requirements.txt") as file:
    requirements = file.read().splitlines()

setup(
    name="LLM-Models",
    version="0.1",
    author="AndV",
    packages=find_packages(),
    install_requires=requirements,
)
