# Viết chương trình nhập vào ma trận A kích cỡ m*n và in ra màn hình
m = int(input("Nhập vào số hàng m của ma trận: "))
n = int(input("Nhập vào số cột n của ma trận: "))

A = []
print("Nhập các phần tử của ma trận:")
for i in range(m):
    row = [] 
    for j in range(n):
        row.append(int(input(f"Nhập phần tử ở vị trí ({i+1},{j+1}): ")))
    A.append(n)

print("Ma trận A là:")
for n in A:
    print(n)
