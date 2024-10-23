import math
# Hàm tính diện tích xung quanh, diện tích toàn phần và thể tích khối trụ
def tinh_khoi_tru(ban_kinh, chieu_cao):
    pi = 3.14
    dien_tich_xung_quanh = 2 * pi * ban_kinh * chieu_cao
    dien_tich_day = pi * ban_kinh ** 2
    dien_tich_toan_phan = dien_tich_xung_quanh + 2 * dien_tich_day
    the_tich = pi * ban_kinh ** 2 * chieu_cao
    
    print(f"Diện tích xung quanh: {round(dien_tich_xung_quanh, 2)}")
    print(f"Diện tích toàn phần: {round(dien_tich_toan_phan, 2)}")
    print(f"Thể tích khối trụ: {round(the_tich, 2)}")

# Nhập bán kính và chiều cao từ bàn phím
ban_kinh = float(input("Nhập bán kính của khối trụ: "))
chieu_cao = float(input("Nhập chiều cao của khối trụ: "))

# Gọi hàm tính toán
tinh_khoi_tru(ban_kinh, chieu_cao)











    
