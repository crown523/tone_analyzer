#!/usr/bin/env python

from distutils.core import setup

# Read the required software from the list.
with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name='tone_analyzer',
    version='1.0',
    description='Tone Analyzer Utility for GT Fangyan Media research group',
    author='Kyle Liang',
    packages=['tone_analyzer'],
    install_requires=[
        requirements
    ]
)