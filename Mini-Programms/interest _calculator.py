#Python compound interest calculator

principe = 0 #сколько денег ты хочешь вложить
rate = 0 #под какой процент
time = 0 #на сколько лет

while True:
    principe = float(input("Enter the principle amount: "))
    if principe <= 0:
        print("Principle can't be less than or equal to zero!")
    else:
        break

while True:
    rate = float(input("Enter the interest rate: "))
    if principe <= 0:
        print("Interest can't be less than or equal to zero!")
    else:
        break

while True :
    time = float(input("Enter the time in years: "))
    if time <= 0:
        print("Time can't be less than or equal to zero!")
    else:
        break

total = principe * pow((1+ rate/100),time)
print(f"Balance after {round(time)} year/s: {total:.2f}$ !")