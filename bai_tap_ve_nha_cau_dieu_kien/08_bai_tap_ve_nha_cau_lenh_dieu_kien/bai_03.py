so_1 = float(input("Nhập số thứ nhất: "))
so_2 = float(input("Nhập số thứ hai: "))
so_3 = float(input("Nhập số thứ ba: "))
# Giả sử số 3 là số lớn nhất
smax = so_3

if so_1 > smax:
    smax = so_1
if so_2 > smax:
    smax = so_2

print("Số lớn nhất trong ba số là:", smax)