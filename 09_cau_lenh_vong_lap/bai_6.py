# Viết chương trình nhập vào một số kiểm tra xem số đó có phải số chính phương hay không?

n= int(input("Nhập số nguyên dương n: "))
for i in range(n):
    if n==i**2:
        print(f"{n} là số chính phương")
        break
else:
    print(f"{n} không là số chính phương")