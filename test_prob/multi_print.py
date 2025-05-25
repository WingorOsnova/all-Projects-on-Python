from test_prob.multi import find_roots
while True:
    pruf = input("Do you want quit? y/n: ").lower()
    if pruf == "y": break
    else:
        a = float(input("Enter a number for a: "))
        b = float(input("Enter a number for b: "))
        c = float(input("Enter a number for c: "))
        find_roots(a,b,c)

