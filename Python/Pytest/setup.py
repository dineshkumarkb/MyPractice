from setuptools import setup,find_packages

# https://stackoverflow.com/questions/17155804/confused-about-the-package-dir-and-packages-settings-in-setup-py

setup(name='mytasks',
    version='0.1.0',
    license='proprietary',
    description='Minimal Project Task Management',
    author='Dinesh',
    packages=['mytasks'],
    package_dir={'mytasks':'src'},
    install_requires=[],
)