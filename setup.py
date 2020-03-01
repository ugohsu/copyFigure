#!/usr/bin/env python3

from distutils.core import setup

setup(
    name="cf",
    version="0.0.1",
    description="copy a figure file into clipboard",
    long_description=open("README.md", "rb").read().decode("utf-8"),
    author="ugos",
    packages=["cf"],
    scripts=["bin/cf", "bin/mathpdf"]
)
