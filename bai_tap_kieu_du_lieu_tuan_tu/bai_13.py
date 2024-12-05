#Bài 13: Viết lệnh thêm một sinh viên vào danh sách sinh viên ở bài 10. Với điều kiện:
# - Nếu tên sinh viên đã tồn tại, thông báo: "Thông tin sinh viên đã tồn tại"
# - Nếu chưa có sinh viên này, thông báo: "Đã thêm sinh viên"

# Danh sách sinh viên và điểm của họ
sinh_vien = [
    {"Ten": "Dung", "Diem": 10.0},
    {"Ten": "Quang", "Diem": 5.3},
    {"Ten": "Trang", "Diem": 7.5}
]

# Nhập tên và điểm của sinh viên cần thêm
ten_moi = input("Nhập tên sinh viên cần thêm: ")
diem_moi = float(input("Nhập điểm của sinh viên: "))

# Kiểm tra xem tên sinh viên đã tồn tại trong danh sách chưa
tontai = False
for sv in sinh_vien:
    if sv['Ten'] == ten_moi:
        tontai = True
        break

# Nếu tên sinh viên chưa tồn tại, thêm sinh viên mới vào danh sách
if tontai:
    print("Thông tin sinh viên đã tồn tại")
else:
    sinh_vien.append({"Ten": ten_moi, "Diem": diem_moi})
    print("Đã thêm sinh viên")

# In danh sách sinh viên sau khi thêm
print("\nDanh sách sinh viên hiện tại:")
for sv in sinh_vien:
    print(f"{sv['Ten']}    {sv['Diem']:.1f}")
