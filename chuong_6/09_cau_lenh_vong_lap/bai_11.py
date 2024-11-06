#Viết chương trình nhập vào hai số bất kì, tìm bội chung nhỏ nhất của hai số đó# Nhập vào 2 số
import math

so1 = int(input("Nhập số thứ nhất: "))
so2 = int(input("Nhập số thứ hai: "))
a = so1
b = so2
# Tìm ước chung lớn nhất bằng pp euclid
while b != 0:
    r = a % b
    a = b
    b = r
# Tính bội chung nhỏ nhất (BCNN)
uoc_chung_lon_nhat = a
boi_chung_nho_nhat = (so1 * so2) // uoc_chung_lon_nhat
print("Bội chung nhỏ nhất của là:", boi_chung_nho_nhat )