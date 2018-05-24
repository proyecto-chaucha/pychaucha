import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="chaucha",
    version="0.0.1dev",
    author="Proyecto Chaucha",
    author_email="dev@chaucha.cl",
    description="Simple tools for working with Chaucha crypto currency",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/proyecto-chaucha/pychaucha",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)