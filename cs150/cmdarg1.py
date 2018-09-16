import sys

def main():
    print ("Command-line arguments counts = ", len(sys.argv))
    print ("Command-line arguments:")

    for i in range(0, len(sys.argv)):
        print ("argv[",i,"]" + " is: ", sys.argv[i])

    return 0

main()
