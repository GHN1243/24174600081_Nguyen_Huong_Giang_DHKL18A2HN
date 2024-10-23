gia_tien_dien = 7000
t = float(input("Thời gian sử dụng điện của bạn là: "))
if t > 0 :
    U = float(input("Nhập điện áp (V): "))
    I = float(input("Nhập cường độ dòng điện (A): "))
    P = U * I
    E = (P * t) / (1000 * 3600)  
    tien_dien = E * gia_tien_dien
    print(f"tiền điện là: {tien_dien:2f} ")
else :
    print("bạn đã nhập sai, hãy nhập lại ")