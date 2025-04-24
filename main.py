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
from tkinter.font import names

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
# validate user input exercise
""""
#1. username is no more than 12 characters
#2. username must not contain spaces
#3. username must not contain digits

username = input("Enter your username: ")
if len(username) > 11:
    print("Your username has more 12 characters")
elif not username.find(" ") == -1:
    print("Your username has a contain spaces!")
elif not username.isalpha():
    print("Your username has a number or char!")
else:
    print(f"All good, nice to meat you {username}")
"""
#string indexing
"""
credit_number = "1234-5678-9012-3456"
#credit_number = credit_number[:: -1]
#print(credit_number)
#last_digits =credit_number[-4:]
#print(credit_number[0:4]) одно и тоде с тем что внизу
#print(f"XXXX-XXXX-XXXX-{last_digits}")
"""
#format specifiers
"""
prise1 = 3.14159
prise2 = -987.65
prise3 = 12.34

# print(f"Price 1 is {prise1:.2f}$") #делает так чтобы после точки оставалось 2 знака
# print(f"Price 2 is {prise2:10}$") #делает строку вообщем 10 символом заполняя их пробелами
# print(f"Price 3 is {prise3:010}$")#делает строку вообщем 10 символом заполняя их нулями

#измениния строки, изменяется откуда начинается строка(ее расположения к краям или центру)
# print(f"Price 1 is {prise1:<10}$")
# print(f"Price 2 is {prise2:>10}$")
# print(f"Price 3 is {prise3:^10}$")

print(f"Price 1 is {prise1:<10}$")
print(f"Price 2 is {prise2:>10}$")
print(f"Price 3 is {prise3:^10}$")
"""
#while loop
"""
name = input("Enter your name: ")
while name =="":
    print("You did not enter your name")
    name = input("Enter your name: ")
print(f"Hello, {name.capitalize()}"
"""
#for loop
"""
for x in range(-10,11,2):
    print(x)
"""

