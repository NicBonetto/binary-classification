from setuptools import setup, find_packages

setup(
    name="binary-classification",
    version="0.0.1",
    description="Basic binary classification ML model",
    packages=find_packages(),
    install_requires=["tensorflow", "keras", "numpy", "matplotlib"]
)
