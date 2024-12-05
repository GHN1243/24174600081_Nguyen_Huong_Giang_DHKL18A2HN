
#Bài 11: Viết lệnh in danh sách sinh viên ở bài 10. Có dạng:
#Ten    Diem
#Dung   10.0
#Quang  5.3
#Trang  7.5

# Danh sách sinh viên và điểm của họ
sinh_vien = [
    {"Ten": "Dung", "Diem": 10.0},
    {"Ten": "Quang", "Diem": 5.3},
    {"Ten": "Trang", "Diem": 7.5}
]

# In tiêu đề
print("Ten    Diem")

# In thông tin từng sinh viên
for sv in sinh_vien:
    # Căn chỉnh tên và điểm sao cho vừa vặn với nhau
    print(f"{sv['Ten']:<7} {sv['Diem']:.1f}")
