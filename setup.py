# setup.py
from setuptools import setup, find_packages

setup(
    name='py_morse',
    version='0.1',
    packages=find_packages(),
    description='A simple package for converting between text and Morse code.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Pratik Kumar',
    author_email='pr2tik1@gmail.com',
    url='https://github.com/pr2tik1/py_morse',
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.8',
    ],
    python_requires='>=3.6',
)
