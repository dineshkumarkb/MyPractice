from setuptools import setup, find_packages

setup(
    name = "ptuple1",
    version = 2.0,
    packages = find_packages(where='src'),
    package_dir = {'':'src'},
    install_requires = []

)