import tkinter as tk
from tkinter import messagebox

def baja_alumno(conexion_db):
    def borrar_alumno():
        matricula = entry_matricula.get()
        
        if not matricula.strip():
            messagebox.showerror("Error", "Por favor ingrese una matrícula")
            return
        
        conn = conexion_db.obtener_conexion()
        if conn:
            try:
                cursor = conn.cursor()
                
                query_verificar = "SELECT * FROM alumnos WHERE matricula = %s"
                cursor.execute(query_verificar, (matricula,))
                result = cursor.fetchone()
                
                if result:
                    confirm = messagebox.askyesno("Confirmar Baja", "¿Está seguro que desea dar de baja al alumno?")
                    if confirm:
                        query_baja = "DELETE FROM alumnos WHERE matricula = %s"
                        cursor.execute(query_baja, (matricula,))
                        conn.commit()
                        messagebox.showinfo("Baja", "Alumno dado de baja correctamente")
                else:
                    messagebox.showerror("Error", "La matrícula no existe en la base de datos")
            except Exception as e:
                messagebox.showerror("Error", f"Error al dar de baja al alumno: {e}")
            finally:
                cursor.close()
        else:
            messagebox.showerror("Error", "No se pudo conectar a la base de datos")

    root = tk.Tk()
    root.title("Baja de Alumno")
    root.geometry("400x300")
    
    tk.Label(root, text="Matrícula").pack(pady=5)
    entry_matricula = tk.Entry(root)
    entry_matricula.pack(pady=5)
    
    tk.Button(root, text="Dar de Baja", command=borrar_alumno).pack(pady=20)
    
    root.mainloop()

if __name__ == "__main__":
    from database import ConexionDB
    
    conexion_db = ConexionDB()
    baja_alumno(conexion_db)
