#!/usr/bin/env python
"""
Setup file for engutils.
"""
import os
import sys

from setuptools import setup

from engutils import __version__, __author__

if __name__ == "__main__":
    with open('README.md', 'r') as file:
        long_description_ = file.read()

    setup(
        name='engutils',
        version=__version__,
        packages=['engutils',],
        description="Importable utilities for engineering problem solving.",
        long_description=long_description_,
        license="MIT License",
        url="https://github.com/MattCJones/engutils",
        author=__author__,
        author_email='matt.c.jones.aoe@gmail.com',
        scripts=None,
        classifiers=[
            "Development Status :: 5 - Production/Stable",
            "Intended Audience :: Science/Research",
            "License :: OSI Approved :: MIT License",
            "Natural Language :: English",
            "Operating System :: OS Independent",
            "Topic :: Scientific/Engineering",
            "Topic :: Utilities",
            "Programming Language :: Python :: 3.7",
            "Programming Language :: Python :: 3.8",
            "Programming Language :: Python :: 3.9",
            ],
        keywords="utility engineering design problem solving",
        install_requires=('pint', 'numpy', 'ambiance'),
    )
