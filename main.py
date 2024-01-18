import sys
import subprocess
import os
import platform
import bpy
import sys
def isWindows():
    return os.name == 'nt'

def isMacOS():
    return os.name == 'posix' and platform.system() == "Darwin"

def isLinux():
    return os.name == 'posix' and platform.system() == "Linux"

def python_exec():
    if isWindows():
        return os.path.join(sys.prefix, 'bin', 'python.exe')
    elif isMacOS():
        try:
            # 2.92 and older
            path = bpy.app.binary_path_python
        except AttributeError:
            # 2.93 and later
            
            path = sys.executable
        return os.path.abspath(path)
    elif isLinux():
        return sys.executable
    else:
        print("Sorry, still not implemented for ", os.name, " - ", platform.system)

def installModule(packageName):
    python_exe = python_exec()
    try:
        subprocess.call([python_exe, "-m", "pip", "install", packageName])
    except Exception as e:
        print(f"Error installing {packageName}: {e}")

installModule("scipy")
