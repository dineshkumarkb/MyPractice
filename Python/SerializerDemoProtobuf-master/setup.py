from distutils.command.build_py import build_py
import os
from setuptools import setup
import subprocess


class GenerateBindings(build_py):
    os.system('echo generating bindings')
    os.system('mkdir -p src-generated/main/python')
    subprocess.Popen('protoc -I=proto-schema --python_out=src-generated/main/python proto-schema/person.proto',shell=True)
    os.system('echo generated bindings')

