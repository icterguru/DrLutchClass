import operator
from List import *

# code from the chapter on recursion

# recursive (functional)
def factorial(n):
  if (n == 0):
      return 1
  else:
      return n * factorial(n - 1)

# using loops (imperative), accumulate pattern
def factorial2(n):
    total = 1;
    for i in range(1,n+1):
       total = total * i
    return total

def gcd(dividend,divisor):
    if (dividend % divisor == 0):
        return divisor
    else:
        gcd(divisor,dividend % divisor)

# version that computes remainder only once
def gcd2(dividend,divisor):
    remainder = dividend % divisor
    if (remainder == 0):
        return divisor
    else:
        return gcd2(divisor,remainder)

# instrumented version
def gcd3(dividend,divisor):
    remainder = dividend % divisor
    print("gcd:",dividend,divisor,remainder)
    if (remainder == 0):
        return divisor
    else:
        return gcd3(divisor,remainder)

# version using a loop
def gcd4(dividend,divisor):
    while (divisor != 0):
        temp = dividend
        dividend = divisor
        divisor = dividend % divisor
    return dividend

# recursive
def fibonacci(n):
    if (n == 0):
        return 0
    elif (n == 1):
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# version using a loop
def fib(n):
    previous = 0
    current = 1
    for i in range(0,n,1):
        temp = previous
        previous = current
        current = previous + temp
    return previous

def ahead(items): return items[0]
def atail(items): return items[1:]  #slicing, which copies!

# counting pattern

# array version
def count(items):
    if (items == []): # base case
        return 0
    else:
        return 1 + count(atail(items))

# list version
def count2(items):
    if (items == None): # base case
        return 0
    else:
        return 1 + count2(tail(items))

# accumulate pattern
def sum(items):
    if (items == None): #base case
        return 0
    else:
        return head(items) + sum(tail(items))

# filtered-count pattern
def countEvens(items):
    if (items == None): #base case
        return 0
    elif (head(items) % 2 == 0):
        return 1 + countEvens(tail(items))
    else:
        return 0 + countEvens(tail(items))

# filtered-count pattern
def occurrences(target,items):
    if (items == None):
        return 0
    elif (head(items) == target):
        return 1 + occurrences(target,tail(items))
    else:
        return occurrences(target,tail(items))

# filtered-accumulate patterns

def sumEvens(items):
    if (items == None):
        return 0
    elif (isEven(head(items))):
        return head(items) + sumEvens(tail(items))
    else:
        return sumEvens(tail(items))

def isEven(x): return x % 2 == 0

# filter pattern
def extractEvens(items):
    if (items == None):
        return None
    elif (isEven(head(items))):
        return join(head(items),extractEvens(tail(items)))
    else:
        return extractEvens(tail(items))

# map pattern
def map(f,items):
    if (items == None):
        return None
    else:
        return join(f(head(items)),map(f,tail(items)))

def decrement(x): return x - 1

# search pattern
def find(target,items):
    return occurrences(target,items) > 0

def find2(target,items):
    if (items == None):
        return False
    elif (head(items) == target):    # short-circuit!
        return True
    else:
        return find2(target,tail(items))

# shuffle pattern (equal length lists)
def shuffle(list1,list2):
    if (list1 == None):
        return None
    else:
        rest = shuffle(tail(list1),tail(list2))
        return join(head(list1),join(head(list2),rest))

# shuffle pattern (general)
def shuffle2(list1,list2):
    if (list1 == None):
        return list2
    elif (list2 == None):
        return list1
    else:
        rest = shuffle2(tail(list1),tail(list2))
        return join(head(list1),join(head(list2),rest))

# simple shuffle (general)
def shuffle3(list1,list2):
    if (list1 == None):
        return list2
    else:
        return join(head(list1),shuffle3(list2,tail(list1)))

# merge pattern
def merge(list1,list2):
    if (list1 == None):
        return list2
    elif (list2 == None):
        return list1
    elif (head(list1) < head(list2)):
        return join(head(list1),merge(tail(list1),list2))
    else:
        return join(head(list2),merge(list1,tail(list2)))

# generic merge pattern
def genericMerge(list1,list2,pred):
    if (list1 == None):
        return list2
    elif (list2 == None):
        return list1
    elif (pred(head(list1),head(list2))):
        return join(head(list1),genericMerge(tail(list1),list2,pred))
    else:
        return join(head(list2),genericMerge(list1,tail(list2),pred))

# fossilized pattern
def factorial3(n):
    if (n == 0):
        return 1
    else:
        return n * factorial3(n) # infinite recursive loop

# bottomless pattern
def div2(n):
    if (n == 0):
        return 0
    else:
        return 1 + div2(n - 2)

def div2instrumented(n):
        print("div2: n is",n)
        if (n == 0):
            return 0
        else:
            return 1 + div2instrumented(n - 2)

def div2correct(n):
    if (n < 2):
        return 0
    else:
        return 1 + div2correct(n - 2)

if (True):
    items = ListCreate(2,5,7,3,8,4,1,6,9,0)
    print("factorial 5:",factorial(5))
    print("factorial 5:",factorial2(5))
    print("gcd 19283,39275:",gcd(19283,39275))
    print("gcd 19283,39275:",gcd2(19283,39275))
    print("gcd 19283,39275:",gcd3(19283,39275))
    print("gcd 19283,39275",gcd4(19283,39275))
    print("fibonacci 5:",fibonacci(5))
    print("fibonacci 5:",fib(5))
    print("items:",items)
    print("count items:",count(items))
    print("count2 items:",count2(items))
    print("sum items:",sum(items))
    print("countEvens items:",countEvens(items))
    print("occurrences 8 items:",occurrences(8,items))
    print("sumEvens items:",sumEvens(items))
    print("extractEvens items:",extractEvens(items))
    print("map decrement items:",map(decrement,items))
    print("find 8 items:",find(8,items))
    print("find2 8 items:",find2(8,items))
    print("shuffle items:",shuffle(items,items))
    print("shuffle2 items:",shuffle2(items,items))
    print("merge [1,[3,[5,None]]]] [2,2,4,4,6,6,8] items:",\
        merge([1,[3,[5,None]]],[2,[2,[4,[4,[6,[6,[8,None]]]]]]]))
    print("genericMerge [1,[3,[5,None]]]] [2,2,4,4,6,6,8] items:",\
        genericMerge([1,[3,[5,None]]],[2,[2,[4,[4,[6,[6,[8,None]]]]]]],operator.lt))
    print("div2correct 333",div2correct(333))
