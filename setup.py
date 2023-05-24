from setuptools import setup

setup(
    name='your-library',
    version='0.1.0',
    description='A Python library for error suggestions using ChatGPT',
    author='Your Name',
    packages=['error_suggester'],
    install_requires=[
        'openai',
        # Add other dependencies here if necessary
    ],
)