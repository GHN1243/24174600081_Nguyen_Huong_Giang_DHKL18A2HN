 #Viết chương trình chuyển đổi hệ cơ số 10 sang hệ cơ số 2 và ngược lại
a = int(input("Nhập một số thập phân: "))
so_dau = ""
n = a

if n == 0:
    so_dau = "0"
else:
    while n > 0:
        so_dau = str(n % 2) + so_dau 
        n = n // 2

print("Hệ nhị phân của", a, "là:", so_dau)