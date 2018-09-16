# source code from the loops chapter
# arrays are expected to be passed as arguments to the following functions

# counting pattern
def countItems(items):
    count = 0
    for i in range(0,len(items),1):
         count += 1
    return count

# filtered-count pattern
def countEvens(items):
    count = 0
    for i in range(0,len(items),1):
        if (items[i] % 2 == 0):
            count += 1
    return count

# accumulate pattern
def sumItems(items):
    total = 0
    for i in range(0,len(items),1):
        total += items[i]
    return total

# filtered-accumulate pattern
def sumEvens(items):
    total = 0
    for i in range(0,len(items),1):
        if (items[i] % 2 == 0):
            total += items[i]
    return total

# searching

# helper function that does a filtered count
def occurrences(target,items):
    count = 0
    for i in range(0,len(items),1):
        if (items[i] == target):
            count = count + 1
    return count

# using a filtered-count to implement search
def find(target,items):
    return occurrences(target,items) > 0

# 'pure' search pattern
def find2(target,items):
    for i in range(0,len(items),1):
        if (items[i] == target):
            return True             # short-circuit!
    return False

# an incorrect search pattern
def find3(target,items):
    for i in range(0,len(items),1):
        if (items[i] == target):
            return True
        else:
            return False


# extreme pattern
def biggest(items):
    largest = items[0]
    for i in range(0,len(items),1):
        if (items[i] > largest):
            largest = items[i]
    return largest

# extreme pattern (one fewer steps)
def biggest2(items):
    largest = items[0]
    for i in range(1,len(items),1): #start comparing at index 1
        if (items[i] > largest):
            largest = items[i]
    return largest

# an incorrect extreme pattern
def biggest3(items):
    largest = 0
    for i in range(0,len(items),1):
        if (items[i] > largest):
            largest = items[i]
    return largest

# extreme-index pattern
def indexOfBiggest(items):
    ilargest = 0
    for i in range(1,len(items),1):
        if (items[i] > items[ilargest]):
            ilargest = i
    return ilargest

def isEven(x): return x % 2 == 0

# filter pattern
def extractEvens(items):
    evens = []
    for i in range(0,len(items),1):
        if (isEven(items[i])):
            evens = evens + [items[i]]
    return evens

# filter pattern - more efficient
def extractEvens2(items):
    evens = []
    for i in range(0,len(items),1):
        if (isEven(items[i])):
            evens.append(items[i])
    return evens

# map pattern
def map(f,items):
    result = []
    for i in range(0,len(items),1):
        transformed = f(items[i])
        result.append(transformed)
    return result

def decrement(x): return x - 1

# shuffle pattern (equal list lengths)
def shuffle(list1,list2):
    list3 = []
    for i in range(0,len(list1),1):
        list3.append(list1[i])
        list3.append(list2[i])
    return list3

# shuffle pattern (general)
def shuffle2(list1,list2):
    list3 = []
    if (len(list1) < len(list2)):
        for i in range(0,len(list1),1):
            list3.append(list1[i])
            list3.append(list2[i])
        return list3 + list2[i+1:]
    else:
        for i in range(0,len(list2),1):
            list3.append(list1[i])
            list3.append(list2[i])
        return list3 + list1[i+1:]

# shuffle pattern (general)
def shuffle3(list1,list2):
    list3 = []
    i = 0
    while (i < len(list1) and i < len(list2)):
        list3.append(list1[i])
        list3.append(list2[i])
        i = i + 1
    return list3 + list1[i:] + list2[i:]

# merge pattern
def merge(list1,list2):
    list3 = []
    i = 0
    j = 0
    while (i < len(list1) and j < len(list2)):
        if (list1[i] < list2[j]):
            list3.append(list1[i])
            i = i + 1
        else:
            list3.append(list2[j])
            j = j + 1
    return list3 + list1[i:] + list2[j:]

if (True):
    items = [2,5,7,3,8,4,1,6,9,0]
    print("items is",items)
    print("countItems:",countItems(items))
    print("countEvens",countEvens(items))
    print("sumItems:",sumItems(items))
    print("sumEvens:",sumEvens(items))
    print("occurrences of 4:",occurrences(4,items))
    print("find 3:",find(3,items))
    print("find2 3:",find2(3,items))
    print("find3 3:",find3(3,items))
    print("biggest:",biggest(items))
    print("biggest2:",biggest2(items))
    print("biggest3:",biggest3(items))
    print("indexOfBiggest:",indexOfBiggest(items))
    print("extractEvens:",extractEvens(items))
    print("extractEvens2:",extractEvens2(items))
    print("map:",map(decrement,items))
    print("shuffle:",shuffle(items,items))
    print("shuffle2:",shuffle2(items,items))
    print("shuffle3:",shuffle3(items,items))
    print("merge [1,3,5] and [2,2,4,4,6,6,8]:",merge([1,3,5],[2,2,4,4,6,6,8]))
