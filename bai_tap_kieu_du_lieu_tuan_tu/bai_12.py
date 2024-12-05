#Bài 12: Viết lệnh xóa thông tin của sinh viên trong danh sách sinh viên ở bài 10 ứng với tên được nhập vào bàn phím
# Danh sách sinh viên và điểm của họ
sinh_vien = [
    {"Ten": "Dung", "Diem": 10.0},
    {"Ten": "Quang", "Diem": 5.3},
    {"Ten": "Trang", "Diem": 7.5}
]

# In danh sách sinh viên ban đầu
print("Danh sách sinh viên trước khi xóa:")
for sv in sinh_vien:
    print(f"{sv['Ten']}    {sv['Diem']:.1f}")

# Nhập tên sinh viên cần xóa
ten_xoa = input("\nNhập tên sinh viên cần xóa: ")

# Xóa sinh viên có tên khớp với tên đã nhập
sinh_vien = [sv for sv in sinh_vien if sv['Ten'] != ten_xoa]

# In danh sách sinh viên sau khi xóa
print("\nDanh sách sinh viên sau khi xóa:")
for sv in sinh_vien:
    print(f"{sv['Ten']}    {sv['Diem']:.1f}")
