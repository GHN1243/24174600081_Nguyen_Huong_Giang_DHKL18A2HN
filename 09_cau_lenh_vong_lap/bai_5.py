# Viết chương trình nhập vào một số kiểm tra xem số đó có phải số hoàn hảo hay không?
n = int(input("Nhập một số: "))
# Tổng các ước
s = 0
if n <= 1:
    print("nhập số nguyên dương")
else:
    # Tìm các ước số
    for i in range(1, n):  # Lặp từ 1 đến n - 1
        if n % i == 0:
            s += i  # Cộng các ước số vào tổng
    if s == n:
        print(f"{n} là số hoàn hảo.")
    else:
        print(f"{n} không phải là số hoàn hảo.")