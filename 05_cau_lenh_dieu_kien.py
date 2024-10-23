#câu lệnh điều kiện
#3 kiểu viết câu lệnh điều kiện
#câu lệnh if... ( sử dụng với 1 điều kiện xét)
#câu lệnh if...else...( sử dụng với 1 điều kiện có và điều kiện)
#câu lệnh if...elif...else ( sử dụng với nhiều điều kiện cần xét)

#xửu lý xoay quanh boolean(True, false)
1  > 2
1  < 2 

#=> trả về kết quả và true hoặc false
# đói với if khi xét điều kiện
# -nếu điều kiện đúng ( true) thì câu lệnh của if sẽ hoạt động
# -nếu điều kiện sai ( flase) thì câu lệnh của if sẽ bị bỏ qua
a = 10
if a > 10:
    print(" Gia tri a thoa man dieu kien ")
    b = a + 1

print ( " ket thuc chuong trinh")

#đói với if ... else khi xét điều kiện 
# nếu điều kiện đúng ( true  ) thì câu lênh của if sẽ hoạt động
# nếu điều kiện sai ( false) thì câu lệnh của else sẽ bị bỏ qua
a = 10
if a > 20:
   print (" gia tri a thoa man")
else:
    print(" gia tri a khong thoa man")

print (" ket thuc chuong tỉnh")

# đối với if... elif... else
# nếu điiều kiện của if đúng thì câu lệnh của if sẽ hoạt đọng
# nếu điều kiện của if sai thì xét tiếp điều kiện của elif
#     nếu điều kiện của elif đúng ( true) thì câu lệnh cảu if sẽ hoạt động
a - 10
if a > 0:
    print( " a la so duong ")
elif a < 0:
    print(" a la so am")
else:
    print (" a la so 0")

print("ket thuc chuong trinh")

# x thuoc khoang ( 2,8] hop [14,24)
# and ( và )
# of ( hoặc )

c = 1
(c > 2 and c <= 8) #(2,8]
(c >= 14 and c < 24) #[14, 24)

(c > 2 and c <= 8) or (c >= 14 and c < 24) #  ( 2,8 ] hop [ 14, 24)
if (c > 2 and c <= 8) or (c >= 14 and c < 24):
    print(" thoa man dieu kien ")


if c > 2 and c <= 8:
   print (" thoa man dieu kien ")
elif c >= 14 and c < 24:
    print (" thoa man dieu kien")
else:
    print(" dieu kien khong thoa man ")
    



