#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='extraction-engine',
    version='0.0.0',
    description='Extract data as json from html web pages using YAML configurations',
    author='Ravi Raja Merugu',
    author_email='ravi@invanalabs.ai',
    url='https://github.com/crawlerflow/extraction-engine',
    packages=find_packages(
        exclude=("dist", "docs", "examples", "tests",)
    ),
    install_requires=[
        'parsel>=1.5.2',
        'pyyaml>=5.1.2'
    ],
    entry_points={
    },
)
