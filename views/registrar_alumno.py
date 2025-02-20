import tkinter as tk
from tkinter import messagebox

def registrar_alumno(conexion_db):
    def guardar_alumno():
        matricula = entries["Matrícula"].get()
        nombre = entries["Nombre"].get()
        apellido_paterno = entries["Apellido Paterno"].get()
        apellido_materno = entries["Apellido Materno"].get()
        grupo = entries["Grupo"].get()
        semestre = entries["Semestre"].get()
        
        conn = conexion_db.obtener_conexion()
        if conn:
            try:
                cursor = conn.cursor()
                query = """
                    INSERT INTO alumnos (matricula, nombre, apellido_paterno, apellido_materno, grupo, semestre)
                    VALUES (%s, %s, %s, %s, %s, %s)
                """
                cursor.execute(query, (matricula, nombre, apellido_paterno, apellido_materno, grupo, semestre))
                conn.commit()
                messagebox.showinfo("Registro exitoso", "Alumno registrado correctamente")
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo registrar al alumno: {e}")
        else:
            messagebox.showerror("Error", "No se pudo conectar a la base de datos")

    root = tk.Tk()
    root.title("Registrar Alumno")
    root.geometry("400x400")
    
    labels = ["Matrícula", "Nombre", "Apellido Paterno", "Apellido Materno", "Grupo", "Semestre"]
    entries = {}
    
    for label in labels:
        tk.Label(root, text=label).pack(pady=5)
        entry = tk.Entry(root)
        entry.pack(pady=5)
        entries[label] = entry
    
    tk.Button(root, text="Guardar", command=guardar_alumno).pack(pady=20)
    
    root.mainloop()
