from List import *

# code from the chapter on lists

def find(value,items):
    spot = items;
    while (spot != None and head(spot) != value):
        spot = tail(spot)
    return spot

def find2(value,items):
    spot = items;
    while (spot != None):
        if (head(spot) == value): return spot
        spot = tail(spot)
    return None

# walking, must have at least 1 node in the list
def getPenultimateNode(items):
    trailing = None;
    leading = items;
    while (tail(leading) != None):
        trailing = leading 
        leading = tail(leading)
    return trailing

# walking, must have at least 2 nodes in the list
def getPenultimateNode2(items):
    trailing = items;
    while (tail(tail(trailing)) != None):
        trailing = tail(trailing)
    return trailing

def countArrayItems(items):
    count = 0
    for i in range(0,len(items),1):
         count += 1
    return count

def countListItems(items):
    count = 0
    spot = items                        #typical list walking initialization
    while (spot != None):               #typical list walking condition
        count += 1
        spot = tail(spot)               #typical list walking update
    return count

def sumArrayEvens(items):
    total = 0
    for i in range(0,len(items),1):
        if (items[i] % 2 == 0):
            total += items[i]
    return total

def sumListEvens(items):
    total = 0
    spot = items
    while (spot != None):
        if (head(spot) % 2 == 0):
            total += head(spot)
        spot = tail(spot)
    return total

def extremeArrayIndex(items):
    ilargest = 0
    for i in range(1,len(items),1):
        if (items[i] > items[ilargest]):
            ilargest = i
    return ilargest

def extremeListIndex(items):
    index = 0
    spot = items
    largest = head(spot)
    ilargest = 0
    while (spot != None):
        if (head(spot) > largest):
            ilargest = index
            largest = head(spot)
        index += 1
        spot = tail(spot)
    return ilargest

def isEven(x): return x % 2 == 0

def extractArrayEvens(items):
    evens = []
    for i in range(0,len(items),1):
        if (isEven(items[i])):
            evens.append(items[i])
    return evens

def extractListEvens(items):
    evens = None
    spot = items
    while (spot != None):
        if (isEven(head(spot))):
            evens = join(head(spot),evens)
        spot = tail(spot)
    return evens

if (True):
    items = ListCreate(2,5,7,3,8,4,1,6,9,0)
    print("items is",items)
    print("find 8:",find(8,items))
    print("find2 8",find2(8,items))
    print("getPenultimateNode:",getPenultimateNode(items))
    print("getPenultimateNode2:",getPenultimateNode2(items))
    print("extractListEvens:",extractListEvens(items))
