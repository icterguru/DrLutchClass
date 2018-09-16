import sys
from scanner import *

def createMatrix(size):
    if size == 0: 
        return []
    else:
        return [0] + createMatrix(size - 1)

def printGrid(gridlist):
    for row in gridlist:
        print (str(row)+"\n")

def nrows(g):
    return len(g)

def ncols(g):
    return len(g[0])

def printMatrix(g):
    for i in range(0,nrows,1):
        for j in range(0,ncols,1):
            print("The original matrix is:",g[i][j])
        print('')
    print('')

def printMatrixTranspose(g):
    for j in range(0,ncols,1):
        for i in range(0,nrows,1):
            print("The transposed matrix is:",g[i][j])
        print('')
    print('')

def readInput(filename,grid):
    s = Scanner(filename)
    r = s.readtoken()
    while r != "":
        r = int(r)
        c = s.readint()
        v = s.readint()
        grid[r][c]=v
        r = s.readtoken()
    s.close()

def main():
    grid = createMatrix(5)
    for i in range(4):
        grid[i] = createMatrix(5)
    readInput(sys.argv[1],grid)
    printMatrixTranspose(g)

main()
