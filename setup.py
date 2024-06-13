from setuptools import setup, find_packages
from typing import List

HYPHEN_E_DOT = '-e .'
def get_requiremnts(file_path=str)->List[str]:
    requirements = []
    with open('requirements.txt') as file_obj:
        requirements = file_obj.readlines()
        requirements=[req.replace("\n"," ") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)


setup(
    name="project",
    version="0.0.1",
    author='Anirudh',
    packages=find_packages(),
    install_requires=get_requiremnts('requirements.txt')
)