#Python weight converter

weight = float(input("Enter your weight: "))
unit = input("Kilograms or Pounds? Enter(K or L): ").upper()

if unit == "K":
    weight = weight * 2.205
    unit= "Lbs"
elif unit == "L":
    weight = weight / 2.205
    unit = "Kgs"
else:
    print(f"{unit} was not valid")
print(f"Your weight is: {round(weight,2)}{unit}")