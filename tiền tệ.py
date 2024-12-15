import tkinter as tk
from tkinter import messagebox

# Tạo từ điển tỷ giá hối đoái các loại tiền
ti_gia_doi = {
    "USD": {"VND": 24000, "EUR": 0.92, "JPY": 140},
    "VND": {"USD": 1/24000, "EUR": 0.000038, "JPY": 0.0058},
    "EUR": {"USD": 1.09, "VND": 27000, "JPY": 150},
    "JPY": {"USD": 0.0071, "VND": 175, "EUR": 0.0067}
}

def chuyen_tien(so_tien, tien_goc, tien_chuyen):
    # kiểm tra xem loại tiền có sẵn không
    if tien_goc not in ti_gia_doi or tien_chuyen not in ti_gia_doi:
        return 'không có sẵn'
    # tiền không được âm
    elif so_tien < 0:
        return 'số tiền phải là số dương'
    # lấy tỉ giá và tính toán
    ti_gia = ti_gia_doi[tien_goc][tien_chuyen]
    a = so_tien * ti_gia
    return a

# Tạo giao diện ứng dụng
class CurrencyConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Currency Converter")

        # Nhập số tiền
        self.amount_label = tk.Label(root, text="Số tiền:")
        self.amount_label.grid(row=0, column=0, pady=10)
        self.amount_entry = tk.Entry(root)
        self.amount_entry.grid(row=0, column=1, pady=10)

        # Nhập loại tiền gốc
        self.from_currency_label = tk.Label(root, text="Tiền gốc:")
        self.from_currency_label.grid(row=1, column=0, pady=10)
        self.from_currency_entry = tk.Entry(root)
        self.from_currency_entry.grid(row=1, column=1, pady=10)

        # Nhập loại tiền muốn chuyển đổi thành
        self.to_currency_label = tk.Label(root, text="Tiền chuyển:")
        self.to_currency_label.grid(row=2, column=0, pady=10)
        self.to_currency_entry = tk.Entry(root)
        self.to_currency_entry.grid(row=2, column=1, pady=10)

        # Nút chuyển đổi
        self.convert_button = tk.Button(root, text="Chuyển đổi", command=self.convert_currency)
        self.convert_button.grid(row=3, column=0, columnspan=2, pady=10)

        # Hiển thị kết quả
        self.result_label = tk.Label(root, text="Kết quả:")
        self.result_label.grid(row=4, column=0, pady=10)
        self.result_value = tk.Label(root, text="")
        self.result_value.grid(row=4, column=1, pady=10)

    def convert_currency(self):
        try:
            so_tien = float(self.amount_entry.get())
            tien_goc = self.from_currency_entry.get().upper()
            tien_chuyen = self.to_currency_entry.get().upper()
            ket_qua = chuyen_tien(so_tien, tien_goc, tien_chuyen)
            self.result_value.config(text=str(ket_qua))
        except ValueError:
            messagebox.showerror("Lỗi", "Vui lòng nhập số tiền hợp lệ.")

# Khởi động giao diện ứng dụng
if __name__ == "__main__":
    root = tk.Tk()
    app = CurrencyConverterApp(root)
    root.mainloop()
