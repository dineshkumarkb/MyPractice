from setuptools import setup

setup(name='maskdata',
      version="1.0",
      description="Anonymization tool for CHA format data",
      author="Dinesh Kumar K B",
      author_email="dineshkumar.kb@ge.com",
      packages=['DataExtractor'],
      scripts='maskdata.py',
      install_requires=['spacy','scispacy'],
      python_requires='>3.4',
       )