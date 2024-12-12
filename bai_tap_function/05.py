# viết hàm kiểm tra một số đó phải số chính phương hay không

import math

def kiem_tra_so_chinh_phuong(n):
    if n < 0:
        return False
    sqrt_n = int(math.sqrt(n))
    return sqrt_n * sqrt_n == n
