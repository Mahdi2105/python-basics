import random as rn        # imports the whole module whihc is called by whatever is after 'as'
from random import randint # imports just a function
from random import *       # imports all functions from random

print('Hello World')

def add2(num):
    return num + 2

# print(add2(6))
# print(add2(4))

print(rn.randint(1, 10))
print(randint(10,20))