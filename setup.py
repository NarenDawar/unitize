from setuptools import setup, find_packages
from pathlib import Path
this_directory = Path(__file__).parent

VERSION = '0.0.6' 
DESCRIPTION = 'A package for unit conversion and casting.'
LONG_DESCRIPTION = (this_directory / "README.md").read_text()

# Setting up
setup(
        name="unitwise", 
        version=VERSION,
        author="Naren Dawar",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        long_description_content_type='text/markdown',
        packages=find_packages(),
        install_requires=[],  
        
        keywords=['python', 'conversion', 'units', 'data', 'time', 'data conversion'],
        classifiers= [
            "Intended Audience :: Education",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)