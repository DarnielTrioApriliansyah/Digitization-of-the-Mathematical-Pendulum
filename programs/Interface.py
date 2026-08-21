import serial
import tkinter as tk
from tkinter import messagebox, ttk

# Inisialisasi koneksi serial
arduino = serial.Serial('COM3', 9600)  # Ganti 'COM3' sesuai port Arduino
arduino.flush()

def mulai_pengukuran():
    try:
        panjang = float(entry_panjang.get())
        periode = int(entry_periode.get())
        
        # Kirim panjang dan periode ke Arduino
        arduino.write(f"{panjang},{periode}\n".encode())
        
        # Tunggu dan terima hasil dari Arduino
        hasil = arduino.readline().decode().strip()  # Baca hasil dari Arduino
        tampilkan_hasil(hasil)  # Tampilkan hasil di GUI

        messagebox.showinfo("Info", "Pengukuran dimulai.")
    except ValueError:
        messagebox.showerror("Error", "Masukkan nilai yang valid.")

def tampilkan_hasil(hasil):
    # Pisahkan hasil menjadi bagian
    data = hasil.split(',')
    panjang = data[0].split('=')[1]
    periode = data[1].split('=')[1]
    gravitasi = data[2].split('=')[1]

    # Tambahkan data ke tabel
    tree.insert('', 'end', values=(panjang, periode, gravitasi))

def reset():
    entry_panjang.delete(0, tk.END)
    entry_periode.delete(0, tk.END)
    tree.delete(*tree.get_children())  # Hapus semua entri di tabel
    entry_panjang.focus()

def tutup_aplikasi():
    arduino.close()
    window.quit()

# GUI
window = tk.Tk()
window.title("Pengukuran Bandul")
window.geometry("500x400")
window.configure(bg="#f0f0f0")

# Frame untuk input
frame_input = tk.Frame(window, bg="#f0f0f0")
frame_input.pack(pady=20)

tk.Label(frame_input, text="Panjang Tali (cm):", bg="#f0f0f0", font=("Helvetica", 12)).grid(row=0, column=0)
entry_panjang = tk.Entry(frame_input, font=("Helvetica", 12), width=10)
entry_panjang.grid(row=0, column=1)

tk.Label(frame_input, text="Periode (detik):", bg="#f0f0f0", font=("Helvetica", 12)).grid(row=1, column=0)
entry_periode = tk.Entry(frame_input, font=("Helvetica", 12), width=10)
entry_periode.grid(row=1, column=1)

# Tombol
frame_buttons = tk.Frame(window, bg="#f0f0f0")
frame_buttons.pack(pady=10)

tk.Button(frame_buttons, text="Mulai", command=mulai_pengukuran, bg="#4CAF50", fg="white", font=("Helvetica", 12)).grid(row=0, column=0, padx=10)
tk.Button(frame_buttons, text="Reset", command=reset, bg="#f44336", fg="white", font=("Helvetica", 12)).grid(row=0, column=1, padx=10)
tk.Button(frame_buttons, text="Keluar", command=tutup_aplikasi, bg="#2196F3", fg="white", font=("Helvetica", 12)).grid(row=0, column=2, padx=10)

# Tabel untuk menampilkan hasil
frame_table = tk.Frame(window, bg="#f0f0f0")
frame_table.pack(pady=20)

# Membuat tabel menggunakan ttk.Treeview
tree = ttk.Treeview(frame_table, columns=("Panjang", "Periode", "Gravitasi"), show='headings')
tree.heading("Panjang", text="Panjang Tali (cm)")
tree.heading("Periode", text="Periode (s)")
tree.heading("Gravitasi", text="Gravitasi (m/s2)")

tree.column("Panjang", anchor='center')
tree.column("Periode", anchor='center')
tree.column("Gravitasi", anchor='center')

tree.pack()

# Fokus pada entry pertama
entry_panjang.focus()

window.mainloop()
