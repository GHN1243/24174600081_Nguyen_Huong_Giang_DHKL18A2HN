import math 
x = float(input("Nhập giá trị x là: "))
F = (-x + (x ** 2 + 4 )**(1/2)) / ((x ** 4 + 1) ** (1/7))
print(f"Giá trị của f(x) là: {f:.2f}")