def countShortTokens(fileName):
    s = Scanner(fileName)

    count = 0
    token = s.readtoken()
    while(token !=""):
        if (len(token) <=SHORT_LIMIT):
            count += 1
        token = s.readtoken()
    s.close()

    return count
