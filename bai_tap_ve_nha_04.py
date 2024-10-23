# Định nghĩa các thông số
dien_ap = 220  # V
cuong_do = 2.7  # A
gia_dien = 7000  # đ/kWh

# Nhập thời gian sử dụng bóng đèn (giây)
thoi_gian = float(input("Nhập thời gian sử dụng bóng đèn (giây): "))

# Tính toán
cong_suat = dien_ap * cuong_do  # W
thoi_gian_gio = thoi_gian / 3600  # giờ
luong_dien_tieu_thu = cong_suat * thoi_gian_gio / 1000  # kWh
tien_dien = luong_dien_tieu_thu * gia_dien  # đ

# Hiển thị kết quả
print(f"Tiền điện phải trả: {round(tien_dien, 2)} đ")
