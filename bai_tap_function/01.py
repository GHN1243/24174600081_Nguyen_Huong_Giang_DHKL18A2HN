# Viết hàm kiểm tra chuỗi kí tự có phải số nguyên

def is_integer_string(n):
    if not n:  # Kiểm tra chuỗi rỗng
        return False
    for c in n:
        if not c.isdigit():
            return False
    return True