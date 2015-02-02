#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name="PythonGithubAPI",
    version="0.1.0",
    author="Nicolas Mendoza",
    author_email="niccolasmendoza@gmail.com",
    description="Library for the Github API",
    long_description=open('README.rst').read(),

    license="MIT License",
    keywords="github api",
    url="https://github.com/nicchub/",
    packages=find_packages(exclude=[]),

    install_requires=['requests >= 2.5',],
    tests_require=['python-coveralls',],

    # https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.2",
        "Topic :: Software Development",
        "Topic :: Software Development :: Libraries"
    ]
)