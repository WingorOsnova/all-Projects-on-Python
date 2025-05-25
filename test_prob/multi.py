import math
def multi2(x,y):
    res = x * y
    return res

def find_roots(a,b,c):
    print(f"Ваш пример: {a}x² + {b}x + {c}")
    diskremenant = b**2-4*a*c
    print(f"D = {diskremenant}")
    if diskremenant > 0:
        x1 = (-b + math.sqrt(diskremenant))/(2 * a)
        x2 = (-b - math.sqrt(diskremenant))/(2 * a)
        print(f"Ваши корни х1: {x1:.2f}, x2: {x2:.2f}")
    elif diskremenant == 0:
        x = -b/(2+a)
        print(f"У вас один корень х: {x:.2f}")
    else:
        real_part = -b / (2 * a)
        imag_part = math.sqrt(-diskremenant) / (2 * a)
        print(f"Комплексные корни: x1 = {real_part:.2f} + {imag_part:.2f}i, x2 = {real_part:.2f} - {imag_part:.2f}i")


