# Viết chương trình nhập vào 2 số bất kì, tìm ước chung lớn nhất của 2 số đó
import math

# Nhập vào 2 số
a = int(input("Nhập số thứ nhất: "))
b = int(input("Nhập số thứ hai: "))

# Tính và in ra GCD sử dụng math.gcd
print("Ước chung lớn nhất của hai số là:", math.gcd(a, b))
