import sys
from cx_Freeze import setup,Executable

build_exe_options = {"packages":["os"]}

base = None

if sys.platform == "win32":
    base = "Win32GUI"

setup(name = "JSON_EDITOR",version = "1.0",script = "my_ui.py", author = "DineshKumar K B",author_email = "dineshkumarkb@gmail.com",options = {"build_exe":build_exe_options},
      executables = [Executable("my_ui.py",targetName = "Json_Editor.exe",icon= "icon.ico",base = base)])