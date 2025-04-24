#🧠 TASK: “Mini-banking.”
""" 
Make a ATM program that:

1)Says hello to the user by name (with f-string and .capitalize())

2)Will ask for an initial balance (use input() + isdigit() to check)

3)Opens the menu in a loop:

1 - View balance

2 - Deposit balance

3 - Withdraw money

4 - Exit

When replenishing - asks for the amount and adds it

When withdrawing - if there is enough money, it withdraws it, otherwise it says “Not enough money”.

When exiting - writes “Goodbye, [name]!” and exits.

📌 Internally use:

while, if, break, continue

int(), isdigit(), abs(), time.sleep()

f“”, .capitalize(), .lower().

round() - round the balance to 2 decimal places
""" #Eng-Doc
"""
Сделай программу-банкомат, которая:

Поздоровается с пользователем по имени (с f-строкой и .capitalize())

Спросит начальный баланс (используй input() + isdigit() для проверки)

Откроет меню в цикле:

1 — Посмотреть баланс

2 — Пополнить баланс

3 — Снять деньги

4 — Выйти

При пополнении — спрашивает сумму и прибавляет

При снятии — если хватает денег, снимает, иначе пишет "Недостаточно средств"

При выходе — пишет “До свидания, [имя]!” и завершает

📌 Внутри используй:

while, if, break, continue

int(), isdigit(), abs(), time.sleep()

f"", .capitalize(), .lower()

round() — округли баланс до 2 знаков после запятой
""" #Rus-Doc
name = input("Good day, enter your name: ")
print(f"Welcome, {name.capitalize()}!")

balance = float(0)
while True:
    initial_balance = input("Enter your initial balance: ")
    try:
        balance = float(initial_balance)
        print(f"On your initial account: {round(balance,2)}$")
        break
    except ValueError:
        print("You have entered invalid symbols. Please enter a number only.")

while True:
    print("Select an action:")
    print("1 - View balance\n2 - Refill balance\n3 - Withdraw money\n4 - Exit")
    action = input()
    if action == "1":
        print(f"On your initial account: {balance}$")
    elif action == "2":
        refill_balance = float(input("Enter the amount of the recharge?: "))
        balance = balance + refill_balance
        print(f"Balance successfully replenished! New balance: {balance}$")
    elif action == "3":
        withdraw_money = float(input("How much do you want to withdraw?: "))
        if withdraw_money > balance:
            print(f"Not enough funds! Balance: {balance}$")
        else:
            balance = balance - withdraw_money
            print(f"You have withdrawn {withdraw_money}, and your account is left with : {balance}")
    elif action == "4":
        print(f"Goodbye, {name.capitalize()}!")
        break
    else:
        print("Invalid option. Please choose from 1 to 4.")
