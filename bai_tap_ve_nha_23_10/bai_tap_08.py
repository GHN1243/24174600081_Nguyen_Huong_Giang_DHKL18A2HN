import math 
x = float(input("Nhập giá trị x: "))
if x > 0 and x != 1:
    G = math.log(4) / math.log(x) + math.log(2) / math.log(x)
    print(f"Giá trị của G là: {G:4.2f}")
else: 
    print("Bạn nhập sai x để thỏa mãn điều kiện ")