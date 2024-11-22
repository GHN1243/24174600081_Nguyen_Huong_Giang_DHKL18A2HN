while True:
    # Nhập hai số m và n
    m = int(input("Nhập số m: "))
    n = int(input("Nhập số n: "))
    
    # Kiểm tra nếu cả m và n đều là số lẻ
    if m % 2 != 0 and n % 2 != 0:
        print("Cả hai số đều là số lẻ. Chương trình dừng.")
        break
    else:
        print("Một hoặc cả hai số không phải là số lẻ. Tiếp tục nhập.")
