# Viết hàm kiểm tra chuỗi kí tự có phải số nguyên dương không

def is_positive_integer(s):
    # Kiểm tra chuỗi có phải là một số nguyên và lớn hơn 0 không
    return s.isdigit() and int(s) > 0
