#!/usr/bin/python
# coding=utf-8

from distutils.core import setup
from pydnspod import __version__


setup(
    name='pydnspod',
    version=__version__,
    description='pydnspod - a dnspod api sdk',
    long_description=open("README.md").read(),
    author='solos',
    author_email='lxl1217@gmail.com',
    packages=["pydnspod"],
    license="MIT",
    platforms=["any"],
    install_requires=['six'],
    url='https://github.com/solos/pydnspod'
)
