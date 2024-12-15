import tkinter as tk
from tkinter import messagebox
import csv
import datetime

def tao_giao_dien():
    root = tk.Tk()
    root.title("Thông Tin Nhân Viên")
    root.geometry('1000x250')

    # Các trường nhập liệu
    cac_truong = [
        ['Mã', 'Tên', 'Ngày sinh', 'Giới tính'],
        ['Đơn vị', 'Số CMND', 'Ngày cấp'],
        ['Chức danh', 'Nơi cấp']
    ]
    cac_o_nhap = {}

    # Tạo các ô tích chọn
    khung_o_tich = tk.Frame(root)
    khung_o_tich.pack(fill='x')
    bien_nhan_vien = tk.BooleanVar()
    bien_nha_cung_cap = tk.BooleanVar()
    tk.Checkbutton(khung_o_tich, text='Nhân viên', variable=bien_nhan_vien).pack(side='left')
    tk.Checkbutton(khung_o_tich, text='Nhà cung cấp', variable=bien_nha_cung_cap).pack(side='left')
    cac_o_nhap['Nhân viên'] = bien_nhan_vien
    cac_o_nhap['Nhà cung cấp'] = bien_nha_cung_cap

    # Tạo các trường nhập liệu
    for hang in cac_truong:
        khung = tk.Frame(root)
        khung.pack(fill='x')
        for truong in hang:
            nhan = tk.Label(khung, text=truong, width=15, anchor='w')
            nhan.pack(side='left')
            if truong == 'Giới tính':
                khung_gioi_tinh = tk.Frame(khung)
                khung_gioi_tinh.pack(side='left')
                bien_gioi_tinh = tk.StringVar()
                tk.Radiobutton(khung_gioi_tinh, text='Nam', variable=bien_gioi_tinh, value='Nam').pack(side='left')
                tk.Radiobutton(khung_gioi_tinh, text='Nữ', variable=bien_gioi_tinh, value='Nữ').pack(side='left')
                cac_o_nhap[truong] = bien_gioi_tinh
            else:
                o_nhap = tk.Entry(khung, width=15)
                o_nhap.pack(side='left')
                cac_o_nhap[truong] = o_nhap

    # Tạo các nút chức năng
    khung_nut = tk.Frame(root)
    khung_nut.pack(fill='x')
    tk.Button(khung_nut, text="Gửi", command=lambda: luu_du_lieu(cac_o_nhap)).pack(side='left')
    tk.Button(khung_nut, text="Sinh nhật hôm nay", command=hien_sinh_nhat_hom_nay).pack(side='left')
    tk.Button(khung_nut, text="Xuất danh sách sắp xếp", command=xuat_danh_sach_sap_xep).pack(side='left')

    root.mainloop()

def luu_du_lieu(cac_o_nhap):
    du_lieu = {truong: o_nhap.get() if truong != 'Giới tính' else o_nhap.get() for truong, o_nhap in cac_o_nhap.items()}
    with open('du_lieu_nhan_vien.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(du_lieu.values())
    messagebox.showinfo("Thành công", "Dữ liệu đã được lưu thành công")

def hien_sinh_nhat_hom_nay():
    hom_nay = datetime.date.today().strftime('%Y-%m-%d')
    with open('du_lieu_nhan_vien.csv', mode='r') as file:
        reader = csv.reader(file)
        sinh_nhat_hom_nay = [row for row in reader if row[4] == hom_nay]
    messagebox.showinfo("Sinh nhật hôm nay", "\n".join([f"{row[1]} ({row[4]})" for row in sinh_nhat_hom_nay]))

def xuat_danh_sach_sap_xep():
    with open('du_lieu_nhan_vien.csv', mode='r') as file:
        reader = csv.reader(file)
        nhan_vien = sorted(reader, key=lambda x: datetime.datetime.strptime(x[4], '%Y-%m-%d'), reverse=True)
    with open('danh_sach_nhan_vien_sap_xep.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(nhan_vien)
    messagebox.showinfo("Thành công", "Danh sách nhân viên đã được xuất và sắp xếp theo tuổi")

# Chạy giao diện
tao_giao_dien()

