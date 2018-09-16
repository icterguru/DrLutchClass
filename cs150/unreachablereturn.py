def testxy(x, y):
    if (y ==0):
        print("A zero value of y, not good!!")
        return 0
    else: 
        print("Non zero value of y, good!!")
        return x/y

    print("The following return is unreachable")
    return 1

#testxy(4, 6)
testxy(4, 0)
