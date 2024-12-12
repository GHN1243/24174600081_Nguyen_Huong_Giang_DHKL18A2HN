# viết hàm kiểm tra số thực
def kiem_tra_so_thuc(n):
    n = n.strip()
    if n.count('.') == 1:
        phan_truoc, phan_sau = n.split('.')
        return phan_truoc.isdigit() and phan_sau.isdigit()
    return False

n = input('Nhập vào giá trị để kiểm tra: ')
if kiem_tra_so_thuc(n):
    print("Đây là số thực")
else:
    print('Đây không phải là số thực')