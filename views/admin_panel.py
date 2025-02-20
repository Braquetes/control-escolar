import tkinter as tk
from views.registrar_alumno import registrar_alumno
from views.consultar_alumno import consultar_alumno
from views.modificar_alumno import modificar_alumno
from views.baja_alumno import baja_alumno

def admin_panel(conexion_db):
    root = tk.Tk()
    root.title("Panel de Administración")
    root.geometry("400x300")
    
    options = [
        ("Registrar Alumno", lambda: registrar_alumno(conexion_db)),
        ("Consultar Alumno", lambda: consultar_alumno(conexion_db)),
        ("Modificar Alumno", lambda: modificar_alumno(conexion_db)),
        ("Baja Alumno", lambda: baja_alumno(conexion_db))
    ]
    
    for option, command in options:
        tk.Button(root, text=option, command=command).pack(pady=5)
    
    root.mainloop()

if __name__ == "__main__":
    from database.db_connection import ConexionDB
    
    conexion_db = ConexionDB()
    admin_panel(conexion_db)
