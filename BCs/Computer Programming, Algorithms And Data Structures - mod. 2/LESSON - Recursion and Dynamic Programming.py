# slides: https://elearning.unipv.it/pluginfile.php/201973/mod_resource/content/1/3%20-%20Recursion.pdf

print("\n" + "--- Recursion ---" + "\n")
# RECURSION
# problem-solving method that consists in breaking a problem down into smaller and smaller sub-problems until you get to a small enough problem that it can be solved trivially

# 1. A recursive algorithm must have a base case
# 2. A recursive algorithm must change its state and move toward the base case
# 3. A recursive algorithm must call itself recursively

print(" \n" + "--- Fibonacci Sequence --- " + " \n ")


def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


nterms = 10
fibo_seq = [fibonacci(n) for n in range(nterms)]

print("Fibonacci sequence: ", fibo_seq)

print(" \n" + "--- Example: Sum og a list of numbers --- " + " \n ")


# iterative solution
def iterative_listsum(numList):
    theSum = 0
    for num in numList:
        theSum = theSum + num
    return theSum


print(iterative_listsum([1, 3, 5, 7, 9]))


# recursive solution
def recursive_listsum(numList):
    if len(numList) == 1:
        return numList[0]
    else:
        return numList[0] + recursive_listsum(numList[1:])


print(recursive_listsum([1, 3, 5, 7, 9]))

print(" \n" + "--- Tower of Hanoi --- " + " \n ")


# TOWER OF HANOI
# if we know how to solve it for n-1 disks we can easily solve it for n disks!

def printMovement(n, source, destination):
    print("Move disk ", n, " from rod ", source, " to rod ", destination)


def TowerOfHanoi(n, source, destination, auxiliary):
    if n == 1:
        printMovement(1, source, destination)
        return
    TowerOfHanoi(n - 1, source, auxiliary, destination)
    printMovement(n, source, destination)
    TowerOfHanoi(n - 1, auxiliary, destination, source)


n = 5
TowerOfHanoi(n, "A", "B", "C")

print(" \n" + "--- Example: Sierpinski Triangle --- " + " \n ")
# https://runestone.academy/ns/books/published/pythonds/Recursion/pythondsSierpinskiTriangle.html
# start with an equilateral triangle
# subdivide it into four smaller congruent equilateral triangles and remove the central triangle
# repeat step 2 with each of the remaining smaller triangle infinitely (or until a specific level)

# each time you create a new set of triangles you recursively apply this procedure to the three smaller corner triangles

import turtle


def drawTriangle(points, color, myTurtle):
    myTurtle.fillcolor(color)
    myTurtle.up()
    myTurtle.goto(points[0][0], points[0][1])
    myTurtle.down()
    myTurtle.begin_fill()
    myTurtle.goto(points[1][0], points[1][1])
    myTurtle.goto(points[2][0], points[2][1])
    myTurtle.goto(points[0][0], points[0][1])
    myTurtle.end_fill()


def getMid(p1, p2):
    return ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)


def sierpinski(points, degree, myTurtle):
    colormap = ['blue', 'red', 'green', 'white', 'yellow',
                'violet', 'orange']
    drawTriangle(points, colormap[degree], myTurtle)
    if degree > 0:
        sierpinski([points[0],
                    getMid(points[0], points[1]),
                    getMid(points[0], points[2])],
                   degree - 1, myTurtle)
        sierpinski([points[1],
                    getMid(points[0], points[1]),
                    getMid(points[1], points[2])],
                   degree - 1, myTurtle)
        sierpinski([points[2],
                    getMid(points[2], points[1]),
                    getMid(points[0], points[2])],
                   degree - 1, myTurtle)


def main():
    myTurtle = turtle.Turtle()
    myWin = turtle.Screen()
    myPoints = [[-100, -50], [0, 100], [100, -50]]
    sierpinski(myPoints, 3, myTurtle)
    myWin.exitonclick()


# main()

# sometimes it is helpful to think of a recursive algorithm in terms of a diagram of function calls


print("\n" + "--- Dynamic Programming ---" + "\n")
# DYNAMIC PROGRAMMING
# approach to solve complex problems splitting them in simpler sub-problems and storing the partial results

# to apply dynamic programming the problem must have the following properties
# 1. Overlapping sub-problems: the solution of the same sub-problems are needed multiple times
# 2. Optimal sub-structure: an optimal solution of the problem can be obtained from optimal solutions of its sub-problems

print(" \n" + "--- Example: Fibonacci Sequence --- " + " \n ")


def dynamic_fibonacci_solution(nTerms):
    f = [0, 1]

    if nTerms <= 1:
        return f[0:nTerms + 1]

    for i in range(2, nTerms + 1):
        f.append(f[i - 1] + f[i - 2])
    return f


nterms = 10
fibo_seq = dynamic_fibonacci_solution(nterms)
print("Fibonacci  sequence: ", fibo_seq)

print(" \n" + "--- Example: Change-making problem --- " + " \n ")


# return 36 cents using these coin values [1, 5, 10, 20]

# simple (greedy) solution:
# 1. chose the largest coin value
# 2. use as many of those as possible
# 3. move to the next lower coins and repeat from point 2

# NOTE: a greedy algorithm does not always produce the optimal solution, but can approximate that solution in a short amount of time
# recursive solutions are very inefficient, too many recursion and partial results recomputed multiple times

# DYNAMIC PROGRAMMING SOLUTION
# 1. Start computing the minimum change for one cent and store it
# 2. repeat adding one cent at a time up to the amount of change we require

def minChangeDP(cointValueList, change):
    minCoins = [0] * (change + 1)
    coinsUsed = [0] * (change + 1)

    for cents in range(change + 1):
        coinCount = cents
        newCoin = 1

        for j in [c for c in cointValueList if c <= cents]:
            if minCoins[cents - j] + 1 < coinCount:
                coinCount = minCoins[cents - j] + 1
                newCoin = j

        minCoins[cents] = coinCount
        coinsUsed[cents] = newCoin

    return minCoins[change], coinsUsed


print(minChangeDP([1, 2, 5, 10, 20, 25, 50, 100], 100))

print(" \n" + "--- Fibonacci recursive --- " + " \n ")


# A naive recursive solution
def fib(n):
    if n == 1 or n == 2:
        result = 1
    else:
        result = fib(n - 1) + fib(n - 2)
    return result


print(fib(7))
print(fib(35))  # takes a while

print(" \n" + "--- Fibonacci memoize --- " + " \n ")


# A memoized solution
def fib_2(n, memo):
    if memo[n] is not None:
        return memo[n]
    if n == 1 or n == 2:
        result = 1
    else:
        result = fib_2(n - 1, memo) + fib_2(n - 2, memo)
    memo[n] = result
    return result


def fib_memo(n):
    memo = [None] * (n + 1)
    return fib_2(n, memo)


print(fib_memo(35))  # fast
print(fib_memo(100))  # fast
# print(fib_memo(1000))  #gives an error, maximum recursion depth


print(" \n" + "--- Fibonacci bottom-up --- " + " \n ")


# A bottom-up solution
def fib_bottom_up(n):
    if n == 1 or n == 2:
        return 1
    bottom_up = [None] * (n + 1)
    bottom_up[1] = 1
    bottom_up[2] = 1
    for i in range(3, n + 1):
        bottom_up[i] = bottom_up[i - 1] + bottom_up[i - 2]
    return bottom_up[n]

print(fib_bottom_up(1000))  #best solution