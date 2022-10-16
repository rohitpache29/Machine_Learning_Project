from importlib.resources import Package
from pytz import VERSION
from setuptools import setup,find_packages 
from typing import List

# declaring variables for setup functions

PROJECT_NAME="housing-predictor"
VERSION="0.0.1"
AUTHOR="Rohit Pache"
DESCRIPTION="This is my first Machine Learning Project that i learned throgh the ineuron"
REQUIREMENT_FILE_NAME="requirements.txt"

def get_requirements_list()->List[str]:
    
    """
    Description: This function is going to return list of requirement 
    mention in requirement.txt file 

    this function is going to return list which contain name of libraries mention in requirements.txt file

    """
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        return requirement_file.readlines().remove("-e .")



setup(

name=PROJECT_NAME,
version=VERSION,
author=AUTHOR,
description=DESCRIPTION,
packages=find_packages(),
install_requires=get_requirements_list()

)

