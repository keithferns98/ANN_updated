from setuptools import setup

with open("README.md", 'r') as f:
    long_description = f.read()

setup(
   name='src',
   version='1.0',
   description='A useful module for Ann package',
   license="MIT",
   long_description=long_description,
   author='Keith',
   author_email='keithfernandes311@gmail.com',
   url="https://github.com/keithferns98/ANN_updated",
   packages=['src'], 
   python_requires=">=3.7", #same as name
   install_requires=[
            "tensorflow",
            "numpy", 
            "pandas",
            "seaborn",
            "matplotlib"], #external packages as dependencies
   scripts=[
            'scripts/cool',
            'scripts/skype',
           ]
)