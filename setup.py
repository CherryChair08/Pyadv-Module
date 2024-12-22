from setuptools import setup, find_packages

setup(
    name="pyadv",
    version="0.1.0",
    description="An Advanced version of python.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/CherryChair08/Pyadv-Module",
    author="Cherry Chair",
    author_email="andrew.cherry.15@bk.ru",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(),
    install_requires=[
        'pyinstaller'
    ],
    python_requires=">=3.6",
)
