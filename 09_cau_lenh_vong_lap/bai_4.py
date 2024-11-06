# Viết chương trình nhập vào một số kiểm tra xem số đó có phải số nguyên tố hay không?

# số nguyên tố là số nguyên dương Lớn hơn 1 và chỉ chia hết cho 1 và chính nó
n = int(input ("Nhập sô nguyên dương n: "))
if n <= 1:
    print( "Đây không phải số nguyên tố ")
else:
    k = n
    for i in range(n) :
        if n % k == 0 and k != n and k != 1:
            print("Đây không phải số nguyên tố")
            break
        k = k - 1
    else:
        print("Đây là số nguyên tố ")
