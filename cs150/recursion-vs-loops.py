#recursive factorial
def factorial(n):
    if (n == 0):
        return 1
    else:
        return n * factorial(n - 1)

#iterative factorial
def factorial(n):
    total = 1
    for i in range(1,n+1,1):
        total *= i
    return total

#recursive greatest common divisor
def gcd(a,b):
    if (b == 0):
        return a
    else:
        return gcd(b,a % b)

#iterative greatest common divisor (broken)
def gcd_bad(a,b):
    while (b != 0):
        a = b
        b = a % b
    return a

#iterative greatest common divisor (broken)
def gcd_bad2(a,b):
    while (b != 0):
        b = a % b
        a = b
    return a

#iterative greatest common divisor (correct)
def gcd(a,b):
    while (b != 0):
        temp = b
        b = a % b
        a = temp
    return a

#iterative greatest common divisor (Python specific swap)
def gcd2(a,b):
    while (b != 0):
        a,b = b,a % b
    return a

#recursive fibonacci (inefficient)
def fib(n):
    if (n < 2):
        return n
    else:
        return fib(n - 1) + fib(n - 2)

#iterative fibonacci
def fib(n):
    a = 0    # the first Fibonacci number
    b = 1    # the second Fibonacci number
    for i in range(0,n,1):
        c = a + b
        a = b
        b = c
    return a

#recursive fibonacci (efficient)
def fib(n):
    def loop(a,b,i):
        if (i < n):
            return loop(b,a + b,i + 1)
        else:
            return a
    return loop(0,1,0)

#recursive factorial
def fact(n):
    total = 1
    for i in range(1,n+1,1):
        total *= i
    return total

#recursive factorial (tail recursive)
def fact2(n):
    def loop(total,i):
        if (i < n + 1):
            return loop(total * i,i + 1)
        else:
            return total
    return loop(1,1)
