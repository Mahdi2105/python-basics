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

# fruit = input('Please enter a fruit')

# if fruit == 'apple':
#     print('the fruit is: ' + fruit)
# else: 
#     print('You did not enter apple, but you entered: ' + fruit)


one_to_ten = randint(1, 10)
 
if one_to_ten == 1:
    print("The roman numeral equivalent of " + str(one_to_ten) + " is I.")
elif one_to_ten == 2:
    print("The roman numeral equivalent of " + str(one_to_ten) + " is II.")
elif one_to_ten == 3:
    print("The roman numeral equivalent of " + str(one_to_ten) + " is III.")
elif one_to_ten == 4:
    print("The roman numeral equivalent of " + str(one_to_ten) + " is IV.")
elif one_to_ten == 5:
    print("The roman numeral equivalent of " + str(one_to_ten) + " is V.")
elif one_to_ten == 6:
    print("The roman numeral equivalent of " + str(one_to_ten) + " is VI.")
elif one_to_ten == 7:
    print("The roman numeral equivalent of " + str(one_to_ten) + " is VII.")
elif one_to_ten == 8:
    print("The roman numeral equivalent of " + str(one_to_ten) + " is VIII.")
elif one_to_ten == 9:
    print("The roman numeral equivalent of " + str(one_to_ten) + " is IX.")
else:
    print("The roman numeral equivalent of " + str(one_to_ten) + " is X.")


# FIZZBUZZ TASK

for num in range(1, 51): # 3rd argument can be added for step i.e range(1, 5, 3) goes up in 3s
    # If num is divisible by both 3 and 5, "FizzBuzz" will be printed.
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    # If num is only divisible by 3, "Fizz" will be printed.
    elif num % 3 == 0:
        print("Fizz")
    # If num is only divisible by 5, "Buzz" will be printed.
    elif num % 5 == 0:
        print("Buzz")
    # num itself will be printed in all other cases.
    else:
        print(num)

the_string = "North Dakota"
print(the_string.rjust(17))  
print(the_string.ljust(17, "*"))  
center_plus = the_string.center(16, "+")  
print(center_plus)
print(the_string.lstrip("North"))
print(center_plus.rstrip("+"))  
print(center_plus.strip("+"))  
print(the_string.replace("North", "South"))  

user_string = "reverse this"
reversed = ""
 
for item in range(len(user_string) - 1, -1, -1): # Starts at the last index,
                                                 # Stops at index before -1 (0, which is first index)
                                                 # Step by -1, goes backwards in index
    reversed += user_string[item]
 
print(reversed)


str_1 = "James Bond is 007."
str_2 = "When the moon hits your eye like a big pizza pie, that's amore!"
str_3 = "Anyway, like I was sayin', shrimp is the fruit of the sea. You can barbecue it, boil it, broil it, bake it, \
saute it. Dey's uh, shrimp-kabobs, shrimp creole, shrimp gumbo. Pan fried, deep fried, stir-fried. There's pineapple \
shrimp, lemon shrimp, coconut shrimp, pepper shrimp, shrimp soup, shrimp stew, shrimp salad, shrimp and potatoes, \
shrimp burger, shrimp sandwich. That- that's about it."
 
# This function reduces the string to letters, numbers, spaces, hyphens, and apostrophes, 
# and assigns that string to the variable spaces_and_letters so that the number of words 
# in it can by found by counting spaces between words.
def word_counter(words):
    spaces_and_letters = ""
    word_count = 1
    for i in words:
        if i.isalnum() or i.isspace() or i == "-" or i == "'":
            spaces_and_letters += i
    for j in spaces_and_letters:
        if j == " ":
            word_count += 1
    return word_count
 
 
print(word_counter(str_1))
print(word_counter(str_2))
print(word_counter(str_3))

name = 'Mahdi'
age = 23

print("{} is {}".format(name, age))

# LISTS AND LIST METHODS

mixed = [10, 4.97, True, "mountain", [9, 8, 7]]
li_str = list("cheese")
print("e" in li_str)
print("a" not in li_str)

up_by_two = [[0, 2], [4, 6], [8, 10], [12, 14]]
print(up_by_two[0])
print(up_by_two[3][1])
furniture = ["chair", "table", "desk", "lamp", "bed"]
print(furniture[-5])
print("Most people own at least " + str(up_by_two[0][1]) + " " + furniture[0] + "s.")
floats = [0.98, 8.76, 6.54, 4.32]
print(floats[1:])
print(floats[1:3])
print(floats[:2])

arctic_animals = ["penguin", "elephant", "polar bear", "walrus", "tiger", "reindeer"]
del arctic_animals[4]
arctic_animals.remove("elephant")
arctic_animals.append("arctic fox")
arctic_animals.insert(2, "snowy owl")  
arctic_animals.sort()  
print(arctic_animals)
print(arctic_animals.index("reindeer"))
print(arctic_animals.pop())