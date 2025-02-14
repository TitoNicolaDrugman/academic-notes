# slides: https://elearning.unipv.it/pluginfile.php/172997/mod_resource/content/6/2%20-%20Linear%20Structures.pdf

# Main linear structures in ADT (algorithm and data structures):
# - Stacks
# - Queues
# - Deques
# - Arrays
# - Lists


# In linear data structures items are arranged sequentially, each item is connected to the previous and the next element
# linear structures have two "ends"


print(" --- Stack ---")
# STACK
# collection of items where the addition of new items and the removal of existing items always takes place at the same end
# !!! the order of insertion is the reverse of the order of removal
# LIFO (Last In, First Out)

from LinearStructures import *

s = Stack()  # creates a new empty stack
s.push(7)  # add a new item on top of the stack
s.pop()  # remove the top item from the stack
s.push("banana")
print(s.peek())  # returns the top item from the stack but does NOT remove it
print(s.isEmpty())  # returns True if the stack is empty, false otherwise
print(s.size())  # returns the number of items in the stack

print(" \n " + " --- Example of a Stack --- " + " \n ")
s2 = Stack()
print(s2.isEmpty())  # return True
s2.push(2)  # stack content [2]
s2.push("hello")  # stack content [2, "hello"]
s2.push(5.4)  # stack content [2, "hello" , 5.4]
print(s2.size())  # returns 3 since there are 3 elements in the stack
print(s2.peek())  # returns 5.4 since is the last element, but does NOT remove it
s2.pop()  # stack content [2, "hello"]

print(" \n" + " --- Problem: balanced parentheses --- " + "\n")
# check id a string contains a balanced number of parentheses

openers = ["(", "[", "{"]
closers = [")", "]", "}"]


def parChecker(symbols_string):
    s3 = Stack()
    balanced = True
    index = 0
    while index < len(symbols_string) and balanced:
        symbol = symbols_string[index]
        if symbol in openers:
            s3.push(symbol)  # if the current symbol is an opening parenthesis, it is pushed in the stack
        else:
            if s3.isEmpty():
                balanced = False
            else:
                top = s3.pop()
                if not matches(top,
                               symbol):  # if the current symbol is a closing, check if the element on top of the...
                    balanced = False  # ... stack is an opening of the correct type
        index = index + 1
    if balanced and s3.isEmpty():
        return True
    else:
        return False


def matches(open, close):  # the match is done comparing the indexes of the two lists corresponding to the...
    return openers.index(open) == closers.index(close)  # ... current open and close elements


print(parChecker("[(){()}]"))  # return True
print(parChecker("[(){()}"))  # return False

print("\n" + "--- Stack ---" + "\n")
# QUEUE
# collection of items where the addition of new items happen at one end ("rear" or "back") and the removal of existing items occurs at the other end ("front")
# the order of insertion is the same of the order or removal
# FIFO: First In, First Out

q = Queue()  # creates a new empty queue
q.enqueue(5)  # adds a new item t to the rear of the queue
q.dequeue()  # removes and returns the front item of the queue
print(q.isEmpty())  # returns True if the queue is empty, False otherwise
print(q.size())  # returns the number of items in the queue

print(" \n " + " --- Example of a Queue --- " + " \n ")
q2 = Queue()
print(q2.isEmpty())  # return True
q2.enqueue(2)  # queue content [2]
q2.enqueue("hello")  # queue content [2, "hello"]
q2.enqueue(5.4)  # queue content [2, "hello", 5.4]
print(q2.size())  # returns 3
q2.dequeue()
print(q2.isEmpty())  # returns False

print(" \n" + " --- Problem: simulate a printer --- " + "\n")
import random


class Printer:
    def __init__(self, max_queue_len):
        self.printQueue = Queue()
        self.max_queue_len = max_queue_len

    def addTask(self, task):
        if self.printQueue.size() < self.max_queue_len:
            self.printQueue.enqueue(task)
            print("Task ", task, " enqueued")
        else:
            print("The queue is full, task ", task, "refused")

    def completeTask(self):
        if not self.printQueue.isEmpty():
            print("Task ", self.printQueue.dequeue(), " printed")


def simulation(tasks_number, max_queue_len):
    myprinter = Printer(max_queue_len)
    tasks_list = list(range(tasks_number, 0, -1))

    while len(tasks_list) >= 0:
        if random.random() >= 0.5:
            myprinter.addTask(tasks_list.pop())
        else:
            myprinter.completeTask()
#simulation(2, 6)

# PRIORITY QUEUE
# particular kind of queue in which
# - each element of the queue has a priority
# - the position of an element in the queue depend on its priority
# - the element with the highest priority is removed first

print("\n" + "--- Deque ---" + "\n")
# DEQUE
# double-ended queue, similar to a queue where items can be added and removed at either the front or the rear
# hybrid between stack and queue

d = Deque()  # creates a new empty deque
d.addFront(1)  # adds a new item to the front of the deque
d.addRear(9)  # adds a new item to the rear od the deque
d.removeFront()  # removes and returns the front item of the deque
d.removeRear()  # removes and returns the rear item of the deque
print(d.isEmpty())  # returns True if the deque is empty, False otherwise
print(d.size())  # returns the number of items in the deque

print(" \n " + " --- Example of a Deque --- " + " \n ")
d2 = Deque()
print(d2.isEmpty())  # returns True
d2.addRear(2)  # Deque content [2]
d2.addRear("hello")  # Deque content ["hello", 2]
d2.addFront(5.4)  # Deque content [5.4, "hello", 2]
print(d2.size())  # returns 3
d2.removeFront()  # Deque content [5.4, "hello"]
d2.removeRear()  # Deque content ["hello"]

print(" \n" + " --- Problem: Palindrome-checker --- " + "\n")

def palchecker(aString):
    charDeque = Deque()
    for ch in aString:
        charDeque.addRear(ch)
    stillEqual = True

    while charDeque.size() > 1 and stillEqual:
        first = charDeque.removeFront()
        last = charDeque.removeRear()
        if first != last:
            stillEqual = False
    return stillEqual

print(palchecker("anna"))
print(palchecker("banana"))

print("\n" + "--- Array ---" + "\n")
# ARRAY
# basic abstract data type that holds an ordered collection of items accessible by an integer index
# array contain elements of homogenous type, all integers, all float...
import numpy as np
# numpy provide the array data structure
arr = np.array([[25, 31, 3], [5,19,28]])
print(arr)

print("\n" + "--- List ---" + "\n")
# LISTS
# collection of items where each item holds a relative position wrt the others
# the first item of a list is generally referred as head
# the last item is generally called end or tail

l = OrderedList()  # creates a new empty ordered list
l.add("hello")  # adds a new item to the list making sure that the order is preserved
l.pop()  # remove the last item on the list
l.pop(7)  # remove the item in position 7
print(l.search("there is no item like this"))  # returns true if the item is present, false otherwise
print(l.index(3))  # returns the position of the item in the list
print(l.isEmpty())  # returns True is the list is empty, False otherwise
print(l.size())  # returns the number of items in the list

print("\n" + "--- Linked List (unordered) ---" + "\n")

# LINKED LISTS (UNORDERED)
# can be unordered or ordered
# linked lists are useful to better understand more complex data structures, like trees and graphs
# unordered: each element is connected to the next one until the last item
# we must maintain the relative position of the items, no need of contiguous memory positioning

# inserting an element at the end of the list is less efficient since we should traverse all the list to reach the last element


