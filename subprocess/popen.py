import subprocess

# program="notepad.exe"
#
# process=subprocess.Popen(program)
#
# code=process.wait()
#
# print(code)

args=['ping','www.yahoo.com']
process=subprocess.Popen(args,stdout=subprocess.PIPE)

data=process.communicate()
for line in data:
    print(line)