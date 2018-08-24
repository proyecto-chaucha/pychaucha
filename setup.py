#!/usr/bin/env python3
# coding: utf-8

from setuptools import find_packages, setup

from chaucha import name, version


setup(
    name=name,
    version=version,
    packages=find_packages(),
    license='MIT',
    author='Camilo Castro',
    author_email='camilo@chaucha.cl',
    description='Provides helper functions to Chaucha',
    url='https://github.com/proyecto-chaucha/pychaucha',
    install_requires=[
        'bitcoin'
    ],
    keywords=['chaucha', 'python3', 'bitcoin', 'cryptocurrency', 'blockchain'],
    include_package_data=True,
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)

