# -*- coding: utf-8 -*-
import subprocess

# code=subprocess.call("notepad.exe")
code=subprocess.call(["ping","www.yahoo.com"])

if code==0:
    print("Success!")
else:
    print("Error")



