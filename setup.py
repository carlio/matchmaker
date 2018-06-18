# -*- coding: utf-8 -*-
# pylint: skip-file
import codecs
import os
import sys
from distutils.core import setup

from setuptools import find_packages

with open("matchmaker/__pkginfo__.py") as f:
    exec(f.read())
_VERSION = globals()["__version__"]

if sys.version_info < (3, 0):
    raise Exception("matching requires Python 3")

_PACKAGES = find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"])

_INSTALL_REQUIRES = []

_CLASSIFIERS = (
    "Development Status :: 1 - Alpha",
    "Environment :: Plugins",
    "Intended Audience :: Developers",
    "Operating System :: OS Independent",
    "Programming Language :: Python :: 3.4",
    "Programming Language :: Python :: 3.5",
    "Programming Language :: Python :: 3.6",
    "License :: OSI Approved :: MIT License",
)

if os.path.exists("README.rst"):
    _LONG_DESCRIPTION = codecs.open("README.rst", "r", "utf-8").read()
else:
    _LONG_DESCRIPTION = "Matching: experimental implementation of a matching engine as a Django app"


setup(
    name="matchmaker",
    version=_VERSION,
    author="Carl Crowder",
    author_email="matchmaker@carlcrowder.com",
    license="MIT",
    zip_safe=False,
    description="Django-based matching engine",
    long_description=_LONG_DESCRIPTION,
    keywords="matching engine django",
    classifiers=_CLASSIFIERS,
    include_package_data=True,
    packages=_PACKAGES,
    install_requires=_INSTALL_REQUIRES,
)
