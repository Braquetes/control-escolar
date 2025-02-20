import tkinter as tk
from tkinter import messagebox
from views.admin_panel import admin_panel

def check_login(user, password, conexion_db):
    conn = conexion_db.obtener_conexion()

    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM administradores WHERE usuario = %s AND contrasena = %s', (user, password))
            result = cursor.fetchone()
            return result is not None
        except Exception as e:
            print(f"Error al ejecutar la consulta: {e}")
            return False
    else:
        return False

def admin_login(conexion_db):
    def login_action():
        user = entry_user.get()
        password = entry_password.get()
        
        if check_login(user, password, conexion_db):
            messagebox.showinfo("Login exitoso", "Bienvenido al panel de administración")
            
            root.after(500, lambda: open_admin_panel(root, conexion_db))
        else:
            messagebox.showerror("Error", "Usuario o contraseña incorrectos")

    root = tk.Tk()
    root.title("Login Administrador")
    root.geometry("400x300")
    
    tk.Label(root, text="Usuario").pack(pady=5)
    entry_user = tk.Entry(root)
    entry_user.pack(pady=5)
    
    tk.Label(root, text="Contraseña").pack(pady=5)
    entry_password = tk.Entry(root, show="*")
    entry_password.pack(pady=5)
    
    tk.Button(root, text="Entrar", command=login_action).pack(pady=20)
    
    root.mainloop()

def open_admin_panel(previous_window, conexion_db):
    previous_window.destroy()
    admin_panel(conexion_db)

if __name__ == "__main__":
    admin_login()
