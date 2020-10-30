import sys
from cx_Freeze import setup,Executable

build_exe_options = {"packages":["os"]}

base = None

if sys.platform == "win32":
    base = "Win32GUI"

setup(name = "Data_Extractor",version = "1.0",script = "maskdata.py",
      author = "DineshKumar K B",
      author_email = "dineshkumarkb@gmail.com",
      options = {"build_exe":build_exe_options},
      executables = [Executable("maskdata.py",targetName = "Data_Extractor.exe",base = base)])