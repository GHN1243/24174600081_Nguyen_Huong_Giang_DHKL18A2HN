x = float(input("Nhập số năm: "))
if x >= 0:
    if (x % 4 == 0 and x % 100 != 0) or (x % 400 == 0):
        print ("Đây là năm nhuận ")
    else:
        print("Đây không là năm nhuận")
else:
    print("Bài toán sai")
print("Kết thúc")