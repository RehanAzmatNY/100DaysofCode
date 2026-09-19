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
