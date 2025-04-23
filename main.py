""""
#Strings
name = "Kostya"; surname = "Lysenko";email = "Kl22@vrun.com"
order = "I want one pizza with Ananas and coca-cola, please."
print(name,surname,email,order, sep="\n")
#Integers
age = 19;quantity = 1
print(f"I am {age} years old.""\n" f"Pizza Shop say: He's want {quantity} pizza")
#float
prise = 9.99
distance = 1.45
print(f"One pizza has prise: {prise}$""\n" f"distance between our Pizza Shop and you're hause is {distance}km.")
#boolean
x = age
if 18<=x<=27:
    print("you're a student, so you'll get a discount(0.99$).")
elif x<18:
    print("You are a kid, i can not you're pizza sell.")
else:
    print("You are NOT a student.")
"""
#Exercise 1 Rectangle Area Calc
"""""
length = float(input("Enter the length: "))
width = float(input("Enter the width: "))
area = length * width
print(f"Answer: {area}cm²") """""
#Exercise 2 Shopping Cart Program
''''
item = input("What item would you like to buy?: ")
prise = float(input("What is the price?: "))
quantity = int(input("How many would you like?: "))
total = prise * quantity
print(f"It will {total}$ cost.") '''
#Exercise 3 Madlibs game - словесна игра.
'''
adjective1 = input("Enter an adjective(desckription): ")
noun1 = input("Enter a noun (person,place,thing): ")
adjective2 = input("Enter an adjective(desckription): ")
verb1 = input("Enter a verb ending with 'ing'): ")
adjective3 = input("Enter an adjective(desckription): ")


print(f"Today I went to a {adjective1} zoo.")
print(f"In an exhibit, i saw a {noun1}")
print(f"{noun1} was {adjective2} and {verb1}")
print(f"i was {adjective3}!")
'''
#Математические действия
"""
import math
a = float(input("Enter the numner of a: "))
b = float(input("Enter the numner of b: "))
c = math.sqrt(pow(a,2) + pow(b,2))
print(f"The side 'c' is: {round(c,1)}cm")
"""




