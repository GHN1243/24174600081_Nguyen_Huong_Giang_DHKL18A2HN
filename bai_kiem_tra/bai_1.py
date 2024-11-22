import math

# Nhập hệ số của phương trình đường thẳng
A = float(input("Nhập hệ số A của đường thẳng (Ax + By + C = 0): "))
B = float(input("Nhập hệ số B của đường thẳng (Ax + By + C = 0): "))
C = float(input("Nhập hệ số C của đường thẳng (Ax + By + C = 0): "))

# Nhập tọa độ tâm và bán kính của đường tròn
h = float(input("Nhập hoành độ của tâm đường tròn (h): "))
k = float(input("Nhập tung độ của tâm đường tròn (k): "))
r = float(input("Nhập bán kính của đường tròn (r): "))

# Tính khoảng cách từ tâm của đường tròn (h, k) đến đường thẳng Ax + By + C = 0
distance = abs(A * h + B * k + C) / math.sqrt(A**2 + B**2)

# Kiểm tra điều kiện tiếp tuyến
if distance == r:
    print("Đường thẳng tiếp tuyến với đường tròn.")
else:
    print("Đường thẳng không tiếp tuyến với đường tròn.")
