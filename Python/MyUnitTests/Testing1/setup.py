from setuptools import setup

setup(
    name = "mycalc",
    version = 1.0,
    author = "Dinesh",
    packages = ['mytasks', 'mynamedtuple'],
    package_dir = {'mytasks':'src',
                   'mynamedtuple':'src'},
    install_requires = []
)