"""
Package configuration.
"""

from setuptools import setup, find_packages

with open('README.md', 'r') as readme_file:
    README = readme_file.read()

setup(
    name='py-jobject',
    version='0.1.0',
    author='Fernando Cicconeto',
    author_email='fcicconeto@gmail.com',
    description= \
        'A package to easily convert between Python objects ' \
        'and JSON-compatible dictionaries, with built-in type conversion.',
    long_description=README,
    long_description_content_type='text/markdown',
    url='https://github.com/fcicc/py-jobject',
    packages=find_packages(),
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ]
)
