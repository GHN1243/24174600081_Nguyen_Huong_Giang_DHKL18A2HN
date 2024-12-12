# viết hàm kiểm tra một số đó phải số chính phương hay không

import math

def is_perfect_square(n):
    if n < 0:
        return False
    sqrt_n = int(math.sqrt(n))
    return sqrt_n * sqrt_n == n
