#Bài 2: Nhập vào dãy A gồm n phần tử từ bàn phím. 
#Tính tổng các phần tử trong dãy A
ds_so = []
while True:
    n = input("Nhap vao so phan tu n trong danh sach: ")
    if n.isdigit() == False:
        print("Yeu cau nhap lai so nguyen duong!!")
    else:
        n = int(n)
        break

for i in range(n):
    while True:
        so = input(f"Nhap gia tri so thu {i + 1}: ")
        if so.isdigit() == False:
            print("Yeu cau nhap vao so!!")
        else:
            so = float(so)
            break
    ds_so.append(so)

tong = sum(ds_so)
print(f"Tong cac so vua nhap: {tong}")




ds_so = []

while True:
    n = input("Nhập vào số phần tử n trong danh sách: ")
    if not n.isdigit():  
        print("Yêu cầu nhập lại số nguyên dương!!")
    else:
        n = int(n)
        break
for i in range(n):
    while True:
        so = input(f"Nhập giá trị số thứ {i + 1}: ")
        if so.lstrip('-').replace('.', '', 1).isdigit():  
            so = float(so)  
            ds_so.append(so)  
            break 
        else:
            print("Bạn hãy nhập lại!")
tong = sum(ds_so)
print(f"Tổng các số vừa nhập: {tong}")