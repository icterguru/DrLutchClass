def main():

    numbers = eval(input("enter a list of numbers enclosed in brackets: "))
    flag = 0
  
    for i in range(1,len(numbers),1):
        if numbers[0] == numbers[i]:
            flag = 1
    if flag == 1:
        print("yes")
    else:
        print("no")


main()

