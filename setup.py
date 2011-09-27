#!/usr/bin/env python

from setuptools import setup, find_packages

import sermepa

setup(
    name='django-sermepa',
    version=".".join(map(str, sermepa.__version__)),
    author='John Boxall',
    author_email='john@handimobility.ca',
    maintainer="Raimon Esteve",
    maintainer_email="resteve@zikzakmedia.com",
    url='https://github.com/zikzakmedia/django-sermepa',
    install_requires=[
        'Django>=1.0'
    ],
    description = 'A pluggable Django application for integrating Sermepa Payments (Servired)',
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Operating System :: OS Independent",
        "Topic :: Software Development"
    ],
)
