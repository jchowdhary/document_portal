# description: This is a Python package setup file for a document processing and retrieval system.
# It includes metadata about the package, such as its name, version, author, and description.
# The package is designed to be installed using setuptools, which is a common tool for packaging Python
# projects. The setup file also specifies that the package should include all sub-packages found in
# the current directory.

from setuptools import setup, find_packages

setup(
    name="document_portal",
    version="0.1",
    author="Jayant",
    author_email='cloudwizkid@gmail.com',
    description="A document processing and retrieval system powered by AI and cloud technologies.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),

)