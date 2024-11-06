 #Tính các phép tính sau

# S1 = 1 + 2 + 3 + 4 + …. + n

# S2 = 1*2*3*4*…*(n-1)

# S3 = 1 – 1/2 + 1/3 – 1/4 + …. + ((-1)**n)/n

# Nhập giá trị n 
n = int(input("Nhập n: "))

# Tính S1
S1 = 0
for i in range(1, n + 1):
    S1 += i  

# Tính S2
S2 = 1
if n > 1: 
    for i in range(1, n):
        S2 *= i

# Tính S3
S3 = 0
for k in range(n):
    S3 += (-1)**k / (k + 1) 

# In kết quả
print(f"S1 = {S1}, S2 = {S2}, S3 = {S3}")


