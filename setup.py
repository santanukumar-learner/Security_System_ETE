from setuptools import setup, find_packages
from typing import List
def get_requirements() -> List[str]:
    """ This function reads the requirements.txt file and 
    returns a list of requirements
    """
    requirement_list:List[str]=[]  
    try:
        with open('requirements.txt', 'r') as f:
            lines =  f.read().splitlines()
            for line in lines:
                requirement = line.strip()
                if requirement and requirement != '-e .':
                    requirement_list.append(requirement)
    
    except FileNotFoundError:
        print("Requirements file not found")
        

setup(
    name='my_package',
    version='0.0.1',
    author='Santanu kumar adhikari',
    author_email='santanukumaradhikari07@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements(),
    # entry_points={
    #     'console_scripts': [
    #         'my_package=my_package.__main__:main'
    #     ]
    # }
)
