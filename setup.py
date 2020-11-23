import re

from setuptools import setup, find_packages

NAME = "test-semrel"
with open("VERSION") as f:
    VERSION = f.read().strip()

setup(
    name=NAME,
    version=VERSION,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
)
