#Viết chương trình nhập vào chuỗi ký tự, trả về chuỗi ký tự sau khi loại bỏ tất cả các dấu cách thừa# Nhập vào họ tên đầy đủ
ho_ten = input("Nhập vào họ tên đầy đủ: ")
danh_sach_tu = ho_ten.split()
ho = danh_sach_tu[0]
ten = danh_sach_tu[-1]
print(f"Ho: {ho}, Ten: {ten}")
