
from setuptools import setup, find_packages
from newapp.core.version import get_version

VERSION = get_version()

f = open('README.md', 'r')
LONG_DESCRIPTION = f.read()
f.close()

setup(
    name='newapp',
    version=VERSION,
    description='MyApp Does Amazing Things!',
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    author='Dinesh Kumar',
    author_email='dineshkumarkb@gmail.com',
    url='https://github.com/johndoe/myapp/',
    license='unlicensed',
    packages=find_packages(exclude=['ez_setup', 'tests*']),
    package_data={'newapp': ['templates/*']},
    include_package_data=True,
    entry_points="""
        [console_scripts]
        newapp = newapp.main:main
    """,
)
