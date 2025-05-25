import tkinter as tk
from tkinter import messagebox
import math


def solve_quadratic():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        c = float(entry_c.get())

        if a == 0:
            messagebox.showerror("Ошибка", "Коэффициент 'a' не может быть 0.")
            return

        D = b ** 2 - 4 * a * c
        if D > 0:
            x1 = (-b + math.sqrt(D)) / (2 * a)
            x2 = (-b - math.sqrt(D)) / (2 * a)
            result = f"Два корня:\nx1 = {x1:.4f}\nx2 = {x2:.4f}"
        elif D == 0:
            x = -b / (2 * a)
            result = f"Один корень:\nx = {x:.4f}"
        else:
            real = -b / (2 * a)
            imag = math.sqrt(-D) / (2 * a)
            result = f"Комплексные корни:\nx1 = {real:.4f} + {imag:.4f}i\nx2 = {real:.4f} - {imag:.4f}i"

        messagebox.showinfo("Результат", result)

        ask_again = messagebox.askyesno("Продолжить?", "Хотите решить другое уравнение?")
        if not ask_again:
            root.destroy()

        # Очистка
        entry_a.delete(0, tk.END)
        entry_b.delete(0, tk.END)
        entry_c.delete(0, tk.END)

    except ValueError:
        messagebox.showerror("Ошибка", "Введите корректные числа.")


# Окно
root = tk.Tk()
root.title("Калькулятор квадратного уравнения")

# Интерфейс
tk.Label(root, text="Введите коэффициенты:").grid(row=0, column=0, columnspan=2)

tk.Label(root, text="a:").grid(row=1, column=0)
entry_a = tk.Entry(root)
entry_a.grid(row=1, column=1)

tk.Label(root, text="b:").grid(row=2, column=0)
entry_b = tk.Entry(root)
entry_b.grid(row=2, column=1)

tk.Label(root, text="c:").grid(row=3, column=0)
entry_c = tk.Entry(root)
entry_c.grid(row=3, column=1)

tk.Button(root, text="Решить", command=solve_quadratic).grid(row=4, column=0, columnspan=2)

root.mainloop()
