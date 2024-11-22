# Viết chương trình nhập vào chuỗi ký tự, đếm xem có bao nhiêu chữ cái viết hoa, bao nhiêu chữ cái viết thường


chuoi_ki_tu = input("Nhập vào chuỗi ký tự: ")
chu_viet_hoa = sum(1 for char in chuoi_ki_tu if char.isupper()) 
chu_viet_thuong = sum(1 for char in chuoi_ki_tu if char.islower())  
print(f"Số chữ cái viết hoa: {chu_viet_hoa}")
print(f"Số chữ cái viết thường: {chu_viet_thuong}")
