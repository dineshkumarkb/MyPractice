from setuptools import setup, find_packages

setup(
    name = "pytest-nice",
    version = 1.0,
    packages = find_packages(where='pytest-nice'),
    package_dir = {'':'pytest-nice'},
    install_requires = []
)