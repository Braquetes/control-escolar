import tkinter as tk
from views.login_admin import admin_login
from views.alumno_panel import student_portal


def open_role_selection(previous_window, conexion_db):
    previous_window.destroy()

    role_window = tk.Tk()
    role_window.title("Seleccionar Rol")
    role_window.geometry("300x200")

    tk.Label(role_window, text="Selecciona tu rol", font=("Helvetica", 14)).pack(pady=20)

    tk.Button(role_window, text="Administrador", command=lambda: open_admin_login(role_window, conexion_db), width=20).pack(pady=10)
    tk.Button(role_window, text="Alumno", command=lambda: open_student_portal(role_window, conexion_db), width=20).pack(pady=10)

    role_window.mainloop()


def open_admin_login(previous_window, conexion_db):
    previous_window.destroy()
    admin_login(conexion_db)


def open_student_portal(previous_window, conexion_db):
    previous_window.destroy()
    student_portal(conexion_db)
