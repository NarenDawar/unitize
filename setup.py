from setuptools import setup, find_packages

VERSION = '0.0.3' 
DESCRIPTION = 'A package for unit conversion and casting.'
LONG_DESCRIPTION = 'This package aims to simplify working with varying units and metrics.'

# Setting up
setup(
        name="unitwise", 
        version=VERSION,
        author="Naren Dawar",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
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