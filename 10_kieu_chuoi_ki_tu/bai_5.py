# Viết chương trình nhập vào chuỗi ký tự, đếm xem có bao nhiêu chữ cái viết hoa, bao nhiêu chữ cái viết thường

# Nhập chuỗi từ người dùng
chuoi_ki_tu = input("Nhập vào chuỗi ký tự: ")

# Đếm số lượng chữ cái viết hoa và viết thường
chu_viet_hoa = sum(1 for char in chuoi_ki_tu if char.isupper())  # Chữ cái viết hoa
chu_viet_thuong = sum(1 for char in chuoi_ki_tu if char.islower())  # Chữ cái viết thường

# In kết quả
print(f"Số chữ cái viết hoa: {chu_viet_hoa}")
print(f"Số chữ cái viết thường: {chu_viet_thuong}")
