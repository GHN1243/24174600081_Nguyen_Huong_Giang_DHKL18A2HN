# viết hàm kiểm tra một số đó phải số nguyên tố hay không
def kiem_tra_so_chinh_phuong(n):
    if n < 0:
        return False
    can = int(n**1/2)
    return can*can == n 
n = int(input("Nhap vao di: "))
if kiem_tra_so_chinh_phuong(n):
    print("Đây là số chính phươngphương")
else:
    print('Đây không phải số chính phương ')