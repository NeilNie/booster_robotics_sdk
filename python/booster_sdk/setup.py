from setuptools import setup, find_packages

setup(
    name="booster_sdk",
    version="0.1.0",
    author="Neil Nie",
    author_email="neilnie@stanford.edu",
    description="A simple SDK for Booster platform",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/booster_sdk",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=[
        # List your dependencies here
    ],
)
