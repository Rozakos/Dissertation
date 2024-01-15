from setuptools import find_packages, setup

def get_requirements(file_path: str) -> list:
    """
    This function returns a list of requirements from the specified file.

    :param file_path: The path to the requirements file.
    :return: A list of requirement strings.
    """
    requirements = []
    with open(file_path) as file:
        requirements = [line.strip() for line in file if line.strip() and line.strip() != '-e .']

    return requirements

setup(
    name="Dissertation",
    version='1.0',
    author='Rozakos',
    author_email='vasileiosrozakos@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
