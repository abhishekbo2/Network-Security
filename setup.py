from setuptools import find_packages, setup
from typing import List

def get_requirements()-> List[str]:
    try: 
        requirements:List[str] = []
        with open("requirements.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                requirement = line.strip()
                if requirement and requirement != '-e .':
                    requirements.append(requirement)
    
    except FileNotFoundError:
        print("the requirements.txt file was not found")
    
    return requirements


setup(
    name = "NetworkSecurity",
    version = "0.0.1",
    author = "Abhi",
    author_email = "abhiabhishek22365@gmail.com",
    packages = find_packages(),
    install_requires = get_requirements()
)