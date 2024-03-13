import random

def setOneDim(r):
    oneDim = input(f"Enter {r} integers: ")
    oneDim = oneDim.split()
    for i in range(len(oneDim)):
        oneDim[i] = int(oneDim[i])
    return oneDim

def printOneDim(oneDim):
    for i in range(len(oneDim)):
        print(oneDim[i], end=" ")
    print()

def setZerosTwoDim(r, c):
    twoDim = []
    for i in range(r):
        t = []
        for j in range(c):
            t.append(0)
        twoDim.append(t)
    return twoDim

def printTwoDim(twoDim):
    for i in range(len(twoDim)):
        for j in range(len(twoDim[i])):
            print(f"{twoDim[i][j]:<4d}", end=" ")
        print()

def doubleColumns(oneDim, twoDim):
    for i in range(len(oneDim)):
        twoDim[i][0] = oneDim[i]
        for j in range(1, len(twoDim[i])):
            twoDim[i][j] = 2 * twoDim[i][j - 1]
    return twoDim

def main():
    r = random.randint(4, 7)
    oneDim = setOneDim(r)
    
    print("oneDim list")
    printOneDim(oneDim)

    c = random.randint(4, 7)
    twoDim = setZerosTwoDim(r, c)
    
    print("Zero twoDim list")
    printTwoDim(twoDim)

    doubleColumns(oneDim, twoDim)
    
    print()
    print("double columns list")
    printTwoDim(twoDim)

if __name__ == "__main__":
    main()
