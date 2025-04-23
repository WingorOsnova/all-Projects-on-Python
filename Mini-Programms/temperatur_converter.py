#Python temp-convector
unit = input("Is this temperature is Celsius or Fahrenheit? Enter(C or F): ")
temp = float(input("Enter your temperature from outside: "))

if unit == "C":
    temp = 9/5 * temp + 32
    unit = "°F"
    print(f"Your temperature outside: {round(temp,2)}{unit}")
elif unit == "F":
    temp = 5/9*(temp - 32)
    unit = "°C"
    print(f"Your temperature outside: {round(temp,2)}{unit}")
else:
    print(f"{unit} was not valid")
