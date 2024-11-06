 #Viết chương trình nhập vào mẫu số và tử số của một phân số, trả về kết quả phân số đã tối giản
import math

tu_so = int(input("nhập vào tử số: "))
mau_so= int(input("nhập vào mẫu số: "))
if mau_so==0:
    print("mẫu số không thể bằng không: ")
else :
    a= tu_so
    b= mau_so
    while b!=0:
        r = a%b
        a=b
        b=r
    uoc_chung_lon_nhat=a
    tu_so_toi_gian = tu_so/uoc_chung_lon_nhat
    mau_so_toi_gian= mau_so/uoc_chung_lon_nhat
    print("Phân số tối giản là:", tu_so_toi_gian, "/", mau_so_toi_gian)
