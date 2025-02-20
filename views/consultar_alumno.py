import tkinter as tk
from tkinter import messagebox

def consultar_alumno(conexion_db):
    def buscar_alumno():
        matricula = entry_matricula.get()
        
        if not matricula.strip():
            messagebox.showerror("Error", "Por favor ingrese una matrícula")
            return
        
        conn = conexion_db.obtener_conexion()
        if conn:
            try:
                cursor = conn.cursor()
                query = """
                SELECT 
                    nombre AS "Nombre", 
                    apellido_paterno AS "Apellido Paterno", 
                    apellido_materno AS "Apellido Materno", 
                    grupo AS "Grupo", 
                    semestre AS "Semestre" 
                FROM alumnos 
                WHERE matricula = %s
                """
                cursor.execute(query, (matricula,))
                result = cursor.fetchone()
                
                if result:
                    labels = ["Nombre", "Apellido Paterno", "Apellido Materno", "Grupo", "Semestre"]
                    details = "\n".join(f"{label}: {value}" for label, value in zip(labels, result))
                    messagebox.showinfo("Consulta - Alumno encontrado", details)
                else:
                    messagebox.showerror("Error", "Matrícula no encontrada")
            except Exception as e:
                messagebox.showerror("Error", f"Error al realizar la consulta: {e}")
            finally:
                cursor.close()
        else:
            messagebox.showerror("Error", "No se pudo conectar a la base de datos")

    root = tk.Tk()
    root.title("Consultar Alumno")
    root.geometry("400x300")
    
    tk.Label(root, text="Matrícula").pack(pady=5)
    entry_matricula = tk.Entry(root)
    entry_matricula.pack(pady=5)
    
    tk.Button(root, text="Buscar", command=buscar_alumno).pack(pady=20)
    
    root.mainloop()

if __name__ == "__main__":
    from database import ConexionDB
    
    conexion_db = ConexionDB()
    consultar_alumno(conexion_db)
