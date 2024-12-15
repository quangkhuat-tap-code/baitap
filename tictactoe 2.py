import tkinter as tk
from tkinter import messagebox
import random

# Khởi tạo cửa sổ chính
root = tk.Tk()
root.title("Tic Tac Toe")
root.geometry("500x600")

# Định nghĩa người chơi và bảng trò chơi
nguoi_choi_1 = "X"
nguoi_choi_2 = "O"
bot = "O"
nguoi_choi_hien_tai = nguoi_choi_1
bang_tro_choi = [" " for _ in range(9)]
che_do_choi = None


# Hàm kiểm tra người thắng cuộc
def kiem_tra_nguoi_thang_cuoc():
    global bang_tro_choi
    dieu_kien_thang = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # hàng ngang
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # hàng dọc
        [0, 4, 8], [2, 4, 6]              # đường chéo
    ]

    for dieu_kien in dieu_kien_thang:
        if bang_tro_choi[dieu_kien[0]] == bang_tro_choi[dieu_kien[1]] == bang_tro_choi[dieu_kien[2]] != " ":
            return bang_tro_choi[dieu_kien[0]]
    return None


# Hàm xử lý sự kiện khi nhấn nút
def khi_nhan_nut(nut, chi_so):
    global nguoi_choi_hien_tai, bang_tro_choi, che_do_choi
    if nut["text"] == " " and bang_tro_choi[chi_so] == " ":
        nut["text"] = nguoi_choi_hien_tai
        bang_tro_choi[chi_so] = nguoi_choi_hien_tai

        nguoi_thang_cuoc = kiem_tra_nguoi_thang_cuoc()
        if nguoi_thang_cuoc:
            label_thong_bao["text"] = f"Người chơi {nguoi_thang_cuoc} thắng! Nhấn vào màn hình để tiếp tục."
            root.bind("<Button-1>", bat_dau_lai_tro_choi)
        elif " " not in bang_tro_choi:
            label_thong_bao["text"] = "Hòa! Nhấn vào màn hình để tiếp tục."
            root.bind("<Button-1>", bat_dau_lai_tro_choi)
        else:
            if che_do_choi == "PvP":
                nguoi_choi_hien_tai = nguoi_choi_2 if nguoi_choi_hien_tai == nguoi_choi_1 else nguoi_choi_1
            elif che_do_choi == "PvB":
                nguoi_choi_hien_tai = bot if nguoi_choi_hien_tai == nguoi_choi_1 else nguoi_choi_1
                if nguoi_choi_hien_tai == bot:
                    nuoc_di_bot()


# Hàm đặt lại trò chơi
def dat_lai_tro_choi():
    global bang_tro_choi, nguoi_choi_hien_tai
    nguoi_choi_hien_tai = nguoi_choi_1
    bang_tro_choi = [" " for _ in range(9)]
    for nut in cac_nut:
        nut["text"] = " "
    label_thong_bao["text"] = ""


# Hàm bắt đầu lại trò chơi khi nhấn vào màn hình
def bat_dau_lai_tro_choi(event):
    root.unbind("<Button-1>")  # Hủy liên kết sự kiện nhấn chuột
    dat_lai_tro_choi()


# Hàm bot thực hiện nước đi
def nuoc_di_bot():
    global nguoi_choi_hien_tai, bang_tro_choi
    cac_nuoc_di_co_san = [i for i in range(9) if bang_tro_choi[i] == " "]
    if cac_nuoc_di_co_san:
        nuoc_di = random.choice(cac_nuoc_di_co_san)
        bang_tro_choi[nuoc_di] = nguoi_choi_hien_tai
        cac_nut[nuoc_di]["text"] = nguoi_choi_hien_tai

        nguoi_thang_cuoc = kiem_tra_nguoi_thang_cuoc()
        if nguoi_thang_cuoc:
            label_thong_bao["text"] = f"Người chơi {nguoi_thang_cuoc} thắng! Nhấn vào màn hình để tiếp tục."
            root.bind("<Button-1>", bat_dau_lai_tro_choi)
        elif " " not in bang_tro_choi:
            label_thong_bao["text"] = "Hòa! Nhấn vào màn hình để tiếp tục."
            root.bind("<Button-1>", bat_dau_lai_tro_choi)
        else:
            nguoi_choi_hien_tai = nguoi_choi_1


# Chọn chế độ chơi
def chon_che_do(che_do):
    global che_do_choi
    che_do_choi = che_do
    if che_do == "PvP":
        label_che_do["text"] = "Chế độ: Người vs Người"
    else:
        label_che_do["text"] = "Chế độ: Người vs Bot"
    khung_che_do.pack_forget()
    khung_tro_choi.pack()


# Tạo lưới nút cho trò chơi
cac_nut = []
khung_tro_choi = tk.Frame(root)
for i in range(9):
    nut = tk.Button(khung_tro_choi, text=" ", font="Helvetica 20", height=3, width=6,  
                    command=lambda i=i: khi_nhan_nut(cac_nut[i], i))
    nut.grid(row=i // 3, column=i % 3)
    cac_nut.append(nut)

# Tạo các nút chọn chế độ
khung_che_do = tk.Frame(root)
nut_pvp = tk.Button(khung_che_do, text="Người vs Người", font="Helvetica 15", command=lambda: chon_che_do("PvP"))
nut_pvp.pack(pady=10)
nut_pvb = tk.Button(khung_che_do, text="Người vs Bot", font="Helvetica 15", command=lambda: chon_che_do("PvB"))
nut_pvb.pack(pady=10)
khung_che_do.pack()

label_che_do = tk.Label(root, text="Chọn chế độ", font="Helvetica 20")
label_che_do.pack(pady=20)

# Tạo nhãn thông báo người thắng
label_thong_bao = tk.Label(root, text="", font="Helvetica 16")
label_thong_bao.pack(pady=20)

# Khởi chạy vòng lặp chính của giao diện
root.mainloop()
