#Viết chương trình nhập vào chuỗi ký tự, trả về số các từ trong chuỗi ký tự vừa nhập
# Nhập vào chuỗi ký tự
chuoi = input("Nhập vào chuỗi ký tự: ")
danh_sach_tu = chuoi.split()
print("Số lượng từ trong chuỗi là:", len(danh_sach_tu))
