# Viết chương trình nhập vào chuỗi ký tự, trả về kết quả đếm số ký tự là chữ, số ký tự là số và số ký tự là ký tự đặc biệt (Không là số, không là chữ) trong chuỗi

chuoi = input("Nhập vào chuỗi ký tự: ")

ki_tu_chu = 0  
ki_tu_so = 0   
ki_tu_dac_biet = 0  

for char in chuoi:
    if char.isalpha():  
        ki_tu_chu += 1
    elif char.isdigit(): 
        ki_tu_so += 1
    elif not char.isspace(): 
        ki_tu_dac_biet += 1

print(f"Số ký tự là chữ: {ki_tu_chu}")
print(f"Số ký tự là số: {ki_tu_so}")
print(f"Số ký tự là ký tự đặc biệt: {ki_tu_dac_biet}")

