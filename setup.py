from typing import List
from setuptools import setup,find_packages

def get_requirements()->List[str]:
    requirement_lst: List[str] = []

    try:
        with open("requirements.txt","r") as file:
            lines = file.readlines()
            for line in lines:
                requirement = line.strip()
                if requirement and requirement != "-e .":
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found!!!")
    return requirement_lst


# print(get_requirements())

setup(
    name="Network Security",
    version="0.0.1",
    author="Jayesh Vengurlekar",
    author_email="jayeshvengurlekar7@gmail.com",
    packages=find_packages(),
    install_requires = get_requirements()
)