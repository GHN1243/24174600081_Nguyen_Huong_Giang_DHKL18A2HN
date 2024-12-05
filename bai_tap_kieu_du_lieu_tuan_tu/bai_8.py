#Bài 8: Viết chương trình đảo vị trí hai cột i, j của ma trận A kích cỡ m*n

# Nhập vào kích thước ma trận m x n
m = int(input("Nhập vào số hàng m của ma trận: "))
n = int(input("Nhập vào số cột n của ma trận: "))

# Nhập ma trận A
print("Nhập các phần tử của ma trận:")
A = []
for i in range(m):
    row = list(map(int, input(f"Nhập hàng {i+1} (các phần tử cách nhau bởi dấu cách): ").split()))
    A.append(row)

# Nhập chỉ số của hai cột cần đảo
i = int(input("Nhập chỉ số cột i (bắt đầu từ 0): "))
j = int(input("Nhập chỉ số cột j (bắt đầu từ 0): "))

# Kiểm tra điều kiện hợp lệ của chỉ số cột
if i < 0 or j < 0 or i >= n or j >= n:
    print("Chỉ số cột không hợp lệ.")
else:
    # Đảo vị trí hai cột i và j
    for row in A:
        row[i], row[j] = row[j], row[i]

    # In ra ma trận sau khi đảo cột
    print("Ma trận sau khi đảo cột:")
    for row in A:
        print(row)
