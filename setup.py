from setuptools import setup, find_packages
from typing import List

hyphen_e_dot = '-e .'

def get_requirements(file_path:str)->List[str]:
    """
    this function will return the list of requirements
    """
    requirement= []
    with open(file_path) as file_obj:
        requirement = file_obj.readlines()
        requirement = [req.replace("\n","") for req in requirement]

        if hyphen_e_dot in requirement:
            requirement.remove(hyphen_e_dot)
    return requirement

setup(
    name="naval",
    version="0.1",
    author='mihir',
    author_email='mihirmaru090@gmail.com',
    packages=find_packages(),
    install_requires= get_requirements('requirements.txt')
)