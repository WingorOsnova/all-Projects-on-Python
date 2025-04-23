#calculator on Python
num1 = float(input("Hello, please enter a 1st number: "))
num2 = float(input("Please enter a 2nd number: "))
operator = input("Enter please a operation for this numbers(+,-,*,/): ")

if operator == "+":
    res1 = num1 + num2
    print(f"Result is: {res1}")
elif operator == "-":
    res2 = num1 - num2
    print(f"Result is: {res2}")
elif operator == "*":
    res3 = num1 * num2
    print(f"Result is: {res3}")
elif operator == "/":
    if num2 == 0:
        print("Error. You can't divide by 0!")
    else:
        res4 = num1 / num2
        print(f"Result is: {res4}")
else:
    print("You have entered the wrong action operator!")