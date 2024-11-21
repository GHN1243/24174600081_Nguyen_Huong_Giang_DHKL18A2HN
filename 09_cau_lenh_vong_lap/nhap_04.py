# tính tổng số nguyên dương
n = int(input(" Nhập số nguyên dương n: "))
S = 0
if n < 0:
    print(" sai")
else:
    for i in range(1, n + 1):
        S += i
    print( f" Tổng là: {S}")
