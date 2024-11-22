# Viết chương trình nhập vào 2 xâu ký tự str_1 và str_2. Kiểm tra xem str_2 có nằm trong str_1 hay không và ngược lại
str_1 = input("Nhập vào xâu ký tự str_1: ")
str_2 = input("Nhập vào xâu ký tự str_2: ")

if str_2 in str_1:
    print(f"'{str_2}' có trong '{str_1}'.")
else:
    print(f"'{str_2}' không có trong '{str_1}'.")

if str_1 in str_2:
    print(f"'{str_1}' có trong '{str_2}'.")
else:
    print(f"'{str_1}' không có trong '{str_2}'.")
