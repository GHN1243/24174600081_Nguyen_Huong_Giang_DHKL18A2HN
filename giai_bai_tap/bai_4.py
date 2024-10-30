# Giải phương trình bậc 2 a*x**2 + b*x + c = 0 ( với a , b, c là số nguyên ) a,b,c là số âm
a = input(" Nhap gia tri a")
b = input(" Nhap gia tri b")
c = input(" Nhap gia tri c")

a = int(a)
b = int(b)
c = int(c)

if a < 0 and b < 0 and c < 0:
    if a !=0:
        delta = b**a - 4*a*c
    else:
        if b !=0:
            