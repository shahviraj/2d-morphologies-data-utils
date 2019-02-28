# Setup.py

from setuptools import setup, find_packages

setup(name='aira-data-utils',
      version='0.1',
      author='Ameya Joshi, Viraj Shah',
      author_email='viraj@iastate.edu',
      url='https://github.com/ameya005/aira-data-utils.git',
      packages=find_packages(),
      install_requires=[
            "astroid==2.2.0",
            "certifi==2018.11.29",
            "chardet==3.0.4",
            "idna==2.8",
            "isort==4.3.9",
            "lazy-object-proxy==1.3.1",
            "mccabe==0.6.1",
            "numpy==1.16.1",
            "pylint==2.3.0",
            "requests==2.21.0",
            "six==1.12.0",
            "typed-ast==1.2.0",
            "urllib3==1.24.1",
            "wrapt==1.11.1",
            "h5py==2.9.0",
            "matplotlib==3.0.2"
            ]
      )

