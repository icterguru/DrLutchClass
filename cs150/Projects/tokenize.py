from scanner import *

def main():
    s = Scanner("test.txt")
    
    count = 0

    token  = s.readtoken()
    tokens = []

    while(token != ""):
        tokens.append(token)
        print (token)
        count += 1
        token = s.readtoken()
        
    print ("Number of total tokens: ", count)
    
    s.close()
    


main()

