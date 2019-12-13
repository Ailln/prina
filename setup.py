from setuptools import setup
from setuptools import find_packages

NAME = "prina"
AUTHOR = "Ailln"
EMAIL = "kinggreenhall@gmail.com"
URL = "https://github.com/Ailln/prina"
LICENSE = "MIT License"
DESCRIPTION = "print python variable with the variable name."

if __name__ == "__main__":
    setup(
        name=NAME,
        version="0.1.3",
        author=AUTHOR,
        author_email=EMAIL,
        url=URL,
        license=LICENSE,
        description=DESCRIPTION,
        packages=find_packages(),
        include_package_data=True,
        install_requires=open("./requirements.txt", "r").read().splitlines(),
        long_description=open("./README.md", "r").read(),
        long_description_content_type='text/markdown',
        zip_safe=True,
        classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
        ]
    )
