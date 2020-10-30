from cx_Freeze import setup,Executable
import sys


base = None

if sys.platform == "win32":
    base = "Win32GUI"


includes = ["speedtest_cli"]

setup(name = "Bandwithtest",
      version = "1.0",
      options = {"build_exe" : {"includes" : includes}},
      executables = [Executable("networktest.py", base = base)])