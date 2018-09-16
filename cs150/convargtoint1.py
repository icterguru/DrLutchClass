import sys

def convargtoint():
    result = []

    for i in range (1, len(sys.argv), 1):
        num = int(sys.argv[i])
        result.append(num)
    return result

def main():

    ints = convargtoint()
    print("Orignial args are :", sys.argv[1:])
    print("converted int args are:", ints)

    return 0

main()
