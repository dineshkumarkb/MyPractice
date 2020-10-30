from setuptools import setup,find_packages

setup(
    name="fixparams",
    version=1.0,
    description="My Unit test samples",
    packages = find_packages(where='src'),
    package_dir = {'':'src'},
    install_requires = []

)