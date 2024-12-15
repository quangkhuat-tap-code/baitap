import tkinter as tk
from tkinter import messagebox

# Khởi tạo khung trò chơi
root = tk.Tk()
root.title("Tic Tac Toe - Choose Mode")

# Chọn chế độ chơi
def chon_che_do(che_do):
    global che_do_choi, bang_tro_choi, grid_size
    che_do_choi = che_do
    khung_che_do.pack_forget()
    if che_do in ["PvP 10x10"]:
        grid_size = 10
    else:
        grid_size = 3
    bang_tro_choi = [" " for _ in range(grid_size * grid_size)]
    tao_luoi(grid_size)
    khung_tro_choi.pack()

# Khởi tạo các biến
nguoi_choi_1 = "X"
nguoi_choi_2 = "O"
bot = "O"
nguoi_choi_hien_tai = nguoi_choi_1
che_do_choi = None
grid_size = 3  # Mặc định là 3x3

# Biến đếm điểm cho chế độ PvP
diem_pvp_nguoi_choi_1 = 0
diem_pvp_nguoi_choi_2 = 0

# Biến đếm điểm cho chế độ PvB
diem_pvb_nguoi_choi = 0
diem_pvb_bot = 0

# Kiểm tra người thắng cuộc cho bản đồ 3x3
def kiem_tra_nguoi_thang_cuoc_3x3():
    global bang_tro_choi
    dieu_kien_thang = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # hàng ngang
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # hàng dọc
        [0, 4, 8], [2, 4, 6]  # đường chéo
    ]

    for dieu_kien in dieu_kien_thang:
        if bang_tro_choi[dieu_kien[0]] == bang_tro_choi[dieu_kien[1]] == bang_tro_choi[dieu_kien[2]] != " ":
            return bang_tro_choi[dieu_kien[0]]
    return None

# Kiểm tra người thắng cuộc cho bản đồ 10x10
def kiem_tra_nguoi_thang_cuoc_10x10():
    global bang_tro_choi, grid_size
    for i in range(grid_size):
        for j in range(grid_size):
            if bang_tro_choi[i * grid_size + j] != " ":
                # Kiểm tra hàng ngang
                if j <= grid_size - 5 and all(bang_tro_choi[i * grid_size + j + k] == bang_tro_choi[i * grid_size + j] for k in range(5)):
                    return bang_tro_choi[i * grid_size + j]
                # Kiểm tra hàng dọc
                if i <= grid_size - 5 and all(bang_tro_choi[(i + k) * grid_size + j] == bang_tro_choi[i * grid_size + j] for k in range(5)):
                    return bang_tro_choi[i * grid_size + j]
                # Kiểm tra đường chéo chính
                if i <= grid_size - 5 and j <= grid_size - 5 and all(bang_tro_choi[(i + k) * grid_size + j + k] == bang_tro_choi[i * grid_size + j] for k in range(5)):
                    return bang_tro_choi[i * grid_size + j]
                # Kiểm tra đường chéo phụ
                if i <= grid_size - 5 and j >= 4 and all(bang_tro_choi[(i + k) * grid_size + j - k] == bang_tro_choi[i * grid_size + j] for k in range(5)):
                    return bang_tro_choi[i * grid_size + j]
    return None

# Tạo lưới nút cho trò chơi
def tao_luoi(grid_size):
    global cac_nut
    cac_nut = []
    for widget in khung_tro_choi.winfo_children():
        widget.destroy()
    for i in range(grid_size * grid_size):
        if grid_size == 3:
            nut = tk.Button(khung_tro_choi, text=" ", font="Helvetica 50", height=100, width=200,
                            command=lambda i=i: khi_nhan_nut(cac_nut[i], i))
        else:
            nut = tk.Button(khung_tro_choi, text=" ", font="Helvetica 15", height=2, width=4,
                            command=lambda i=i: khi_nhan_nut(cac_nut[i], i))
            nut.grid(row=i // grid_size, column=i % grid_size)
            cac_nut.append(nut)

# Xử lý sự kiện khi nhấn nút
def khi_nhan_nut(nut, chi_so):
    global nguoi_choi_hien_tai, bang_tro_choi, che_do_choi
    global diem_pvp_nguoi_choi_1, diem_pvp_nguoi_choi_2, diem_pvb_nguoi_choi, diem_pvb_bot
    if nut["text"] == " " and bang_tro_choi[chi_so] == " ":
        nut["text"] = nguoi_choi_hien_tai
        bang_tro_choi[chi_so] = nguoi_choi_hien_tai

        if grid_size == 3:
            nguoi_thang_cuoc = kiem_tra_nguoi_thang_cuoc_3x3()
        else:
            nguoi_thang_cuoc = kiem_tra_nguoi_thang_cuoc_10x10()

        if nguoi_thang_cuoc:
            if che_do_choi in ["PvP 3x3", "PvP 10x10"]:
                if nguoi_thang_cuoc == nguoi_choi_1:
                    diem_pvp_nguoi_choi_1 += 1
                elif nguoi_thang_cuoc == nguoi_choi_2:
                    diem_pvp_nguoi_choi_2 += 1
                messagebox.showinfo("Kết thúc trò chơi", f"Người chơi {nguoi_thang_cuoc} thắng!\n"
                                                          f"Tỷ số - Người chơi 1: {diem_pvp_nguoi_choi_1}, Người chơi 2: {diem_pvp_nguoi_choi_2}")
            elif che_do_choi in ["PvB 3x3"]:
                if nguoi_thang_cuoc == nguoi_choi_1:
                    diem_pvb_nguoi_choi += 1
                elif nguoi_thang_cuoc == bot:
                    diem_pvb_bot += 1
                messagebox.showinfo("Kết thúc trò chơi", f"Người chơi {nguoi_thang_cuoc} thắng!\n"
                                                          f"Tỷ số - Người chơi: {diem_pvb_nguoi_choi}, Bot: {diem_pvb_bot}")
            reset_tro_choi()
        elif " " not in bang_tro_choi:
            messagebox.showinfo("Kết thúc trò chơi", "Hoà!")
            reset_tro_choi()
        else:
            if che_do_choi in ["PvP 3x3", "PvP 10x10"]:
                nguoi_choi_hien_tai = nguoi_choi_2 if nguoi_choi_hien_tai == nguoi_choi_1 else nguoi_choi_1
            elif che_do_choi in ["PvB 3x3"]:
                nguoi_choi_hien_tai = bot if nguoi_choi_hien_tai == nguoi_choi_1 else nguoi_choi_1
                if nguoi_choi_hien_tai == bot:
                    nuoc_di_bot()

# Hàm xác định nước đi của bot
def nuoc_di_bot():
    def minimax(bang_tro_choi, is_maximizing):
        winner = kiem_tra_nguoi_thang_cuoc_3x3() if grid_size == 3 else kiem_tra_nguoi_thang_cuoc_10x10()
        if winner == 'X':
            return -1
        elif winner == 'O':
            return 1
        elif " " not in bang_tro_choi:
            return 0

        if is_maximizing:
            best_score = -float('inf')
            for i in range(grid_size * grid_size):
                if bang_tro_choi[i] == " ":
                    bang_tro_choi[i] = 'O'
                    score = minimax(bang_tro_choi, False)
                    bang_tro_choi[i] = " "
                    best_score = max(score, best_score)
            return best_score
        else:
            best_score = float('inf')
            for i in range(grid_size * grid_size):
                if bang_tro_choi[i] == " ":
                    bang_tro_choi[i] = 'X'
                    score = minimax(bang_tro_choi, True)
                    bang_tro_choi[i] = " "
                    best_score = min(score, best_score)
            return best_score

    global bang_tro_choi, nguoi_choi_hien_tai, diem_pvb_bot
    best_move = None
    best_score = -float('inf')

    for i in range(grid_size * grid_size):
        if bang_tro_choi[i] == " ":
            bang_tro_choi[i] = 'O'
            score = minimax(bang_tro_choi, False)
            bang_tro_choi[i] = " "
            if score > best_score:
                best_score = score
                best_move = i

    if best_move is not None:
        bang_tro_choi[best_move] = 'O'
        cac_nut[best_move]["text"] = 'O'

        nguoi_thang_cuoc = kiem_tra_nguoi_thang_cuoc_3x3() if grid_size == 3 else kiem_tra_nguoi_thang_cuoc_10x10()
        if nguoi_thang_cuoc:
            if nguoi_thang_cuoc == bot:
                diem_pvb_bot += 1
            messagebox.showinfo("Kết thúc trò chơi", f"Người chơi {nguoi_thang_cuoc} thắng!\n"
                                                      f"Tỷ số - Người chơi: {diem_pvb_nguoi_choi}, Bot: {diem_pvb_bot}")
            reset_tro_choi()
        elif " " not in bang_tro_choi:
            messagebox.showinfo("Kết thúc trò chơi", "Hòa!")
            reset_tro_choi()
        else:
            nguoi_choi_hien_tai = nguoi_choi_1

# Reset trò chơi
def reset_tro_choi():
    global bang_tro_choi, nguoi_choi_hien_tai
    bang_tro_choi = [" " for _ in range(grid_size * grid_size)]
    nguoi_choi_hien_tai = nguoi_choi_1
    for nut in cac_nut:
        nut["text"] = " "

# Tạo lưới nút cho trò chơi
def tao_luoi(grid_size):
    global cac_nut
    cac_nut = []
    for widget in khung_tro_choi.winfo_children():
        widget.destroy()
    for i in range(grid_size * grid_size):
        nut = tk.Button(khung_tro_choi, text=" ", font="Helvetica 15", height=2, width=4,
                        command=lambda i=i: khi_nhan_nut(cac_nut[i], i))
        nut.grid(row=i // grid_size, column=i % grid_size)
        cac_nut.append(nut)

# Tạo các nút chọn chế độ
khung_che_do = tk.Frame(root)
nut_pvp_3x3 = tk.Button(khung_che_do, text="Player vs Player 3x3", font="Helvetica 15", command=lambda: chon_che_do("PvP 3x3"))
nut_pvp_3x3.pack(pady=10)
nut_pvb_3x3 = tk.Button(khung_che_do, text="Player vs Bot 3x3", font="Helvetica 15", command=lambda: chon_che_do("PvB 3x3"))
nut_pvb_3x3.pack(pady=10)
nut_pvp_10x10 = tk.Button(khung_che_do, text="Player vs Player 10x10", font="Helvetica 15", command=lambda: chon_che_do("PvP 10x10"))
nut_pvp_10x10.pack(pady=10)

khung_che_do.pack()

# Khởi chạy vòng lặp chính của giao diện
khung_tro_choi = tk.Frame(root)
root.mainloop()

