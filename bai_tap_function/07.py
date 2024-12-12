# viết hàm tìm ước chung lớn nhất của 2 số nguyên bất kì

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
