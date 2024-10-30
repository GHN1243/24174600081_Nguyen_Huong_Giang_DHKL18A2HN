import math
# Nhập tọa độ điểm M và tâm I và bán kính R
x = float(input("Nhập tọa độ x của điểm M: "))
y = float(input("Nhập tọa độ y của điểm M: "))
a = float(input("Nhập tọa độ x của tâm I: "))
b = float(input("Nhập tọa độ y của tâm I: "))
R = float(input("Nhập bán kính R: "))
# Tính khoảng cách điểm M và tâm I
do_dai = math.sqrt((x - a) ** 2 + (y - b) ** 2)
# Kiểm tra điểm M có nằm trong hoặc trên hình tròn không
if do_dai <= R:
    print(True)
else:
    print(False)