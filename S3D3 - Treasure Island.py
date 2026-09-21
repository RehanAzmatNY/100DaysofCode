#conditional if/else statements
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height > 120:
    print("You can ride the rollercoaster!")
else:
    print("Sorry, you are not tall enough to ride the rollercoaster.")

#Comparison operators - > < >= <= == !=
#Modulo operator - % (returns the remainder of a division)
number_to_check = int(input("what is the number you want to check? "))

print(number_to_check % 2) #returns 0 if even, 1 if odd
if number_to_check % 2 == 0:
    print("The number is EVEN.")
else:
    print("The number is ODD.")

#Nested if statement - If statements inside of if statements
if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:                    #if yor age is less than 12, you pay $5
        print("Please pay $5.")
    elif age <= 18:                 #if your age is less than or equal to 18, you pay $7
        print("Please pay $7.")
    else:                           #if your age is greater than 18, you pay $12
        print("Please pay $12.")
else:
    print("Sorry, your ass isn't tall enough to ride the rollercoaster.")   #if your height is less than 120, you cannot ride the rollercoaster

#Exercise from earlier in this module
# weight = 85
# height = 1.85

# bmi = weight / (height ** 2)

# # 🚨 Do not modify the values above
# # Write your code below 👇

# if bmi < 18.5:                    #NOTE THE INDENTATION - the code inside the if statement is indented
# 	print("underweight")
# elif bmi < 25:
# 	print("normal weight")
# else:
#     print("overweight")

#Python Pizza Deliveries! program
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
pepperoni = input("Do you want pepperoni? Y or N ")
extracheese = input("Do you want extra cheese? Y or N ")

#todo: work out how much they need to pay based on their size choice
if size == "S":
    bill = 15
elif size == "M":
    bill = 20
else:
    bill = 25

#todo: work out how much to add to their bill based on their pepperoni choice
if pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

#todo: work out their final amount based on whether if they want extra cheese or not
if extracheese == "Y":
    bill += 1

print(f"Your final bill is: ${bill}")

#Treasure Island Game (Choose your own adventure game)
#if you want to include ' in your text, then use \ Ex- you\'re = you're
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print("You are at a crossroad. Where do you want to go? Type 'left' or 'right'")
choice1 = input("Type your choice: ").lower()   #.lower converts the input to lowercase
if choice1 == "left":
    print("You come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across.")
    choice2 = input("Type your choice: ").lower()
    if choice2 == "wait":
        print("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?")
        choice3 = input("Type your choice: ").lower()
        if choice3 == "red":
            print("It's a room full of fire. Game Over.")
        elif choice3 == "yellow":
            print("You found the treasure! You Win!")
        elif choice3 == "blue":
            print("You enter a room of beasts. Game Over.")
        else:
            print("You chose a door that doesn't exist. Game Over.")
    else:
        print("You get attacked by an angry trout. Game Over.")
