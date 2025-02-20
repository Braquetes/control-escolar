import tkinter as tk
from PIL import Image, ImageTk
from database.db_connection import ConexionDB
from views.menu import open_role_selection


def main_window():
    conexion_db = ConexionDB()

    root = tk.Tk()
    root.title("Control Escolar - Prepa 181")
    root.geometry("400x300")

    tk.Label(root, text="Control Escolar", font=("Helvetica", 16)).pack(pady=10)
    tk.Label(root, text="Prepa 181", font=("Helvetica", 12)).pack(pady=5)

    img = Image.open("logo.png")
    img = img.resize((300, 300))
    logo = ImageTk.PhotoImage(img)

    tk.Label(root, image=logo).pack(pady=5)

    tk.Button(root, text="Acceder", command=lambda: open_role_selection(root, conexion_db), width=20).pack(pady=20)

    root.mainloop()


if __name__ == "__main__":
    main_window()
