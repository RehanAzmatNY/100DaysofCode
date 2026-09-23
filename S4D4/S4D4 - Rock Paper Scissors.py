import random                        #random module is responsible for generating random numbers                
import My_Module

random_integer = random.randint(1,10)   #random numbers from 1-10
print("your random number is:", random_integer)                   #python module is responsible for a different piece of functionality
print(My_Module.my_favorite_number)     #importing a module allows you to use the functions and variables defined in that module

random_number_0_to_1 = random.random()   #random numbers from 0-1
print("your random number from 0-1 is:", random_number_0_to_1)


random_integer = random.randint(1,2)   #random numbers from 1-2
if random_integer == 1:
    print("You flipped: heads")
else:
    print("You flipped: tails")
    