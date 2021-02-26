"""
Handles setup for the module
"""
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ed-engineer-shopping-list-builder",
    version="1.0.0",
    author="Brett Ammeson",
    author_email="ammesonb@gmail.com",
    description=(
        "A helper with intelligent prompts to build the ED engineer shopping list, "
        "since the UI is a pain to add multiples of components"
    ),
    long_description=long_description,
    url="https://github.com/ammesonb/ed-engineer-shopping-list-builder",
    packages=setuptools.find_packages(),
    python_requires=">=3.7",
)
