
from scanner import *

def main():
    s = Scanner("file1.py")
    
    b = s.readbool()
    i = s.readint()
    f = s.readfloat()
    str = s.readstring()
    t = s.readtoken()
    
    print("The type of",b,"is",type(b))
    print("The type of",i,"is",type(i))
    print("The type of",f,"is",type(f))
    print("The type of",str,"is",type(str))
    print("The type of",t,"is",type(t))
    s.close()
    return 0

main()

