import os
from example1 import debug    

cwd = os.getcwd()
print(cwd)
abpath = os.path.abspath('resume.doc')
print(abpath)
t = os.listdir(cwd)
print(t)

for i in t:
    if os.path.isdir(i):
        print(i ,"is a directory")
    elif os.path.isfile(i):
        print(i ,"is a file")
    else:
        print("No such file or directory found")
        
        
@debug        
def add(x,y):
    print (x + y)

@debug
def sub(x,y):
    print (x - y)

def main():
    add(3,4)
    sub(7,3)


main()
