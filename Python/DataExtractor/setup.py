from setuptools import setup
import setuptools

setup(name='maskdata',
      version=1.0,
      description='Anonymization Tool',
      author='Dinesh Kumar',
      author_email='dineshkumar.kb@ge.com',
      packages= setuptools.find_packages(),
      # scripts=['maskdata/maskdata.py'],
      license ='MIT',
      classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
       ],
      install_requires=[
            'numpy',
            'pandas',
            'spacy',
            'sqlalchemy'
      ],
      dependency_links =['https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-2.1.0/en_core_web_sm-2.1.0.tar.gz'],
      python_requires='>=3.4',
      )