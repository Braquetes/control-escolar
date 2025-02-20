import tkinter as tk
from tkinter import messagebox

def modificar_alumno(conexion_db):
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
                SELECT nombre, apellido_paterno, apellido_materno, grupo, semestre 
                FROM alumnos 
                WHERE matricula = %s
                """
                cursor.execute(query, (matricula,))
                result = cursor.fetchone()
                
                if result:
                    entry_nombre.insert(0, result[0])
                    entry_apellido_paterno.insert(0, result[1])
                    entry_apellido_materno.insert(0, result[2])
                    entry_grupo.insert(0, result[3])
                    entry_semestre.insert(0, result[4])
                else:
                    messagebox.showerror("Error", "Matrícula no encontrada")
            except Exception as e:
                messagebox.showerror("Error", f"Error al buscar el alumno: {e}")
            finally:
                cursor.close()
        else:
            messagebox.showerror("Error", "No se pudo conectar a la base de datos")

    def actualizar_alumno():
        matricula = entry_matricula.get()
        nombre = entry_nombre.get()
        apellido_paterno = entry_apellido_paterno.get()
        apellido_materno = entry_apellido_materno.get()
        grupo = entry_grupo.get()
        semestre = entry_semestre.get()
        
        if not all([matricula, nombre, apellido_paterno, apellido_materno, grupo, semestre]):
            messagebox.showerror("Error", "Todos los campos son obligatorios")
            return
        
        conn = conexion_db.obtener_conexion()
        if conn:
            try:
                cursor = conn.cursor()
                query = """
                UPDATE alumnos 
                SET nombre = %s, apellido_paterno = %s, apellido_materno = %s, grupo = %s, semestre = %s 
                WHERE matricula = %s
                """
                cursor.execute(query, (nombre, apellido_paterno, apellido_materno, grupo, semestre, matricula))
                conn.commit()
                messagebox.showinfo("Actualización", "Datos actualizados correctamente")
            except Exception as e:
                messagebox.showerror("Error", f"Error al actualizar los datos: {e}")
            finally:
                cursor.close()
        else:
            messagebox.showerror("Error", "No se pudo conectar a la base de datos")

    root = tk.Tk()
    root.title("Modificar Alumno")
    root.geometry("400x500")
    
    # Entrada para la matrícula
    tk.Label(root, text="Matrícula").pack(pady=5)
    entry_matricula = tk.Entry(root)
    entry_matricula.pack(pady=5)
    
    # Botón para buscar al alumno
    tk.Button(root, text="Buscar", command=buscar_alumno).pack(pady=10)
    
    # Campos para modificar los datos
    tk.Label(root, text="Nombre").pack(pady=5)
    entry_nombre = tk.Entry(root)
    entry_nombre.pack(pady=5)
    
    tk.Label(root, text="Apellido Paterno").pack(pady=5)
    entry_apellido_paterno = tk.Entry(root)
    entry_apellido_paterno.pack(pady=5)
    
    tk.Label(root, text="Apellido Materno").pack(pady=5)
    entry_apellido_materno = tk.Entry(root)
    entry_apellido_materno.pack(pady=5)
    
    tk.Label(root, text="Grupo").pack(pady=5)
    entry_grupo = tk.Entry(root)
    entry_grupo.pack(pady=5)
    
    tk.Label(root, text="Semestre").pack(pady=5)
    entry_semestre = tk.Entry(root)
    entry_semestre.pack(pady=5)
    
    tk.Button(root, text="Guardar Cambios", command=actualizar_alumno).pack(pady=20)
    
    root.mainloop()

if __name__ == "__main__":
    from database import ConexionDB
    
    conexion_db = ConexionDB()
    modificar_alumno(conexion_db)
