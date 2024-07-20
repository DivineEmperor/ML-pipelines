from setuptools import setup, find_packages

def get_requirements(file='requirements.txt'):
    with open('requirements.txt') as f:
        return f.read().splitlines()
setup(
    name='project1',
    version='0.1',
    packages=find_packages(),
    author='Pavan',
    install_requires= get_requirements()
)