from setuptools import setup

setup(
    name = "pytest-nice",
    version = 1.0,
    py_modules = ['pytest_nice'],
    entry_points = {'pytest11':["nice = pytest_nice",],}
)