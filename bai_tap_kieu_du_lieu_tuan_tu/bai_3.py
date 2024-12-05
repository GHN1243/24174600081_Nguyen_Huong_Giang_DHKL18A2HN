#Bài 3: Nhập vào số nguyên dương n.
#In ra màn hình: 
# - Danh sách A gồm các số lẻ nhỏ hơn n
# - Danh sách B gồm các số chẵn nhỏ hơn n
#Sắp xếp dãy số theo thứ tự giảm dần

n = int(input("Nhập vào số nguyên dương n: "))
A = [i for i in range(1, n) if i % 2 != 0]
B = [i for i in range(2, n) if i % 2 == 0]

A.sort(reverse=True)
B.sort(reverse=True)

print("Danh sách A (số lẻ nhỏ hơn n):", A)
print("Danh sách B (số chẵn nhỏ hơn n):", B)
