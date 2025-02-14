# https://youtu.be/wMNrSM5RFMc

# Example, find 5!
# find an algorithm to find factorial for any number n!

# An iterative (= looping) algorithm
def get_iterative_factorial(n):
    if n < 0:
        return -1
    else:
        fact = 1
        for i in range(1, n+1):
            fact *= i
        return fact

print(get_iterative_factorial(8))


# A recursive Algorithm
# recursive function: breaks the problem down into smaller problems and calls itself for each of the smaller problems
# it includes a base case (or terminal case) and a recursive case


# PROS & CONS
# CON: no calculation is done until the base case is reached, for very large problems you may run out of memory (millions of open functions calls)
# CON: sometimes more abstract or harder to understand than iterative solutions
# PRO: extremely fast and easy to code. Extremely practical for tree traversals and binary search

def get_recursive_factorial(n):
    if n < 0:  # for errors
        return -1
    elif n < 2:  # for base cases
        return 1
    else:
        return n*get_recursive_factorial(n-1)

print(get_recursive_factorial(8))