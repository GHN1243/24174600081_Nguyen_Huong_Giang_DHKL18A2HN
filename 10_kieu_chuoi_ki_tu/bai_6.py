# Viết chương trình nhập vào chuỗi ký tự, kiểm tra xem chuỗi đó có phải là số âm hay không

chuoi = input("Nhập vào chuỗi ký tự: ")

# Kiểm tra xem chuỗi có phải là số âm không
if chuoi.startswith('-') and chuoi[1:].isdigit():
    print("Chuỗi là số âm.")
else:
    print("Chuỗi không phải là số âm.")
