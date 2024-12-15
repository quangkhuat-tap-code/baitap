import tkinter as tk
from tkinter import messagebox


# Khởi tạo khung trò chơi
root = tk.Tk()
root.title("Tic Tac Toe - Choose Mode")

# Chọn chế độ chơi
def chon_che_do(che_do):
    global che_do_choi
    che_do_choi = che_do
    khung_che_do.pack_forget()
    khung_tro_choi.pack()

# Khởi tạo các biến
nguoi_choi_1 = "X"
nguoi_choi_2 = "O"
bot = "O"
nguoi_choi_hien_tai = nguoi_choi_1
bang_tro_choi = [" " for _ in range(9)]
che_do_choi = None

# Kiểm tra người thắng cuộc
def kiem_tra_nguoi_thang_cuoc():
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

# Xử lý sự kiện khi nhấn nút
def khi_nhan_nut(nut, chi_so):
    global nguoi_choi_hien_tai, bang_tro_choi, che_do_choi
    if nut["text"] == " " and bang_tro_choi[chi_so] == " ":
        nut["text"] = nguoi_choi_hien_tai
        bang_tro_choi[chi_so] = nguoi_choi_hien_tai

        nguoi_thang_cuoc = kiem_tra_nguoi_thang_cuoc()
        if nguoi_thang_cuoc:
            messagebox.showinfo("Kết thúc trò chơi", f"Người chơi {nguoi_thang_cuoc} thắng!")
            reset_tro_choi()
        elif " " not in bang_tro_choi:
            messagebox.showinfo("Kết thúc trò chơi", "Hoà!")
            reset_tro_choi()
        else:
            if che_do_choi == "PvP":
                nguoi_choi_hien_tai = nguoi_choi_2 if nguoi_choi_hien_tai == nguoi_choi_1 else nguoi_choi_1
            elif che_do_choi == "PvB":
                nguoi_choi_hien_tai = bot if nguoi_choi_hien_tai == nguoi_choi_1 else nguoi_choi_1
                if nguoi_choi_hien_tai == bot:
                    nuoc_di_bot()


# Hàm xác định nước đi của bot
def nuoc_di_bot():
    def minimax(bang_tro_choi, is_maximizing):
        if kiem_tra_nguoi_thang_cuoc_bot('X'):
            return -1
        elif kiem_tra_nguoi_thang_cuoc_bot('O'):
            return 1
        elif " " not in bang_tro_choi:
            return 0

        if is_maximizing:
            best_score = -float('inf')
            for i in range(9):
                if bang_tro_choi[i] == " ":
                    bang_tro_choi[i] = 'O'
                    score = minimax(bang_tro_choi, False)
                    bang_tro_choi[i] = " "
                    best_score = max(score, best_score)
            return best_score
        else:
            best_score = float('inf')
            for i in range(9):
                if bang_tro_choi[i] == " ":
                    bang_tro_choi[i] = 'X'
                    score = minimax(bang_tro_choi, True)
                    bang_tro_choi[i] = " "
                    best_score = min(score, best_score)
            return best_score

    def kiem_tra_nguoi_thang_cuoc_bot(nguoi_choi):
        dieu_kien_thang = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # hàng ngang
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # hàng dọc
            [0, 4, 8], [2, 4, 6]  # đường chéo
        ]
        for dieu_kien in dieu_kien_thang:
            if bang_tro_choi[dieu_kien[0]] == bang_tro_choi[dieu_kien[1]] == bang_tro_choi[dieu_kien[2]] == nguoi_choi:
                return True
        return False

    global bang_tro_choi, nguoi_choi_hien_tai
    best_move = None
    best_score = -float('inf')

    for i in range(9):
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

        nguoi_thang_cuoc = kiem_tra_nguoi_thang_cuoc()
        if nguoi_thang_cuoc:
            messagebox.showinfo("Kết thúc trò chơi", f"Người chơi {nguoi_thang_cuoc} thắng!")
            reset_tro_choi()
        elif " " not in bang_tro_choi:
            messagebox.showinfo("Kết thúc trò chơi", "Hòa!")
            reset_tro_choi()
        else:
            nguoi_choi_hien_tai = nguoi_choi_1


# Reset trò chơi
def reset_tro_choi():
    global bang_tro_choi, nguoi_choi_hien_tai
    nguoi_choi_hien_tai = nguoi_choi_1
    bang_tro_choi = [" " for _ in range(9)]
    for nut in cac_nut:
        nut["text"] = " "

# Tạo lưới nút cho trò chơi
cac_nut = []
khung_tro_choi = tk.Frame(root)
for i in range(9):
    nut = tk.Button(khung_tro_choi, text=" ", font="Helvetica 30", height=5, width=10,
                    command=lambda i=i: khi_nhan_nut(cac_nut[i], i))
    nut.grid(row=i // 3, column=i % 3)
    cac_nut.append(nut)

# Tạo các nút chọn chế độ
khung_che_do = tk.Frame(root)
nut_pvp = tk.Button(khung_che_do, text="Player vs Player", font="Helvetica 15", command=lambda: chon_che_do("PvP"))
nut_pvp.pack(pady=10)
nut_pvb = tk.Button(khung_che_do, text="Player vs Bot", font="Helvetica 15", command=lambda: chon_che_do("PvB"))
nut_pvb.pack(pady=10)

khung_che_do.pack()

# Khởi chạy vòng lặp chính của giao diện
root.mainloop()
