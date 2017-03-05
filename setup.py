#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from __future__ import absolute_import, print_function

import io
import re
from os.path import dirname
from os.path import join

from setuptools import setup, find_packages


def read(*names, **kwargs):
    return io.open(
        join(dirname(__file__), *names),
        encoding=kwargs.get("encoding", "utf8")
    ).read()


setup(
    name='deepforest',
    url="https://github.com/nitlev/deepforest",
    author='Veltin DUPONT',
    author_email='veltind@gmail.com',
    classifiers=[
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Data scientists',
        'Topic :: Deep Learning :: Q learning',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3.5',
    ],
    keywords='random forest :: deep learning',
    version='0.1.0',
    license='BSD',
    description='This is a simple implementation of the deep forest method',
    long_description=re.compile('^.. start-badges.*^.. end-badges',
                                re.M | re.S).sub('', read('README.md')),
    packages=find_packages(),
    install_requires=read('requirements.txt').split("\n"),
    extras_require={},
)