# Viết chương trình nhập vào chuỗi ký tự, trả về chuỗi ký tự sau khi loại bỏ tất cả các dấu cách thừa
# Ví dụ: Nhập vào: “Hom nay    troi   mua   ”
#              Trả về: “Hom nay troi mua”

# Nhập chuỗi từ người dùng
chuoi_ki_tu_ban_dau  = input("Nhập vào chuỗi ký tự: ")

# Loại bỏ dấu cách thừa (dùng split để tách các từ và join để nối lại)
chuoi_sau_khi_xoa = " ".join(chuoi_ki_tu_ban_dau.split())

# In ra chuỗi kết quả
print("Chuỗi sau khi loại bỏ dấu cách thừa:", chuoi_sau_khi_xoa )
