import tkinter as tk
from tkinter import messagebox
from views.alumno_info import alumno_info


def student_portal(conexion_db):
    def obtener_datos_alumno():
        matricula = entry_matricula.get().strip()
        if not matricula:
            messagebox.showerror("Error", "Por favor, ingresa una matrícula válida.")
            return
        
        conn = conexion_db.obtener_conexion()
        try:
            cursor = conn.cursor()
            consulta = """
                SELECT matricula, nombre, apellido_paterno, apellido_materno, grupo, semestre
                FROM alumnos
                WHERE matricula = %s
            """
            cursor.execute(consulta, (matricula,))
            resultado = cursor.fetchone()

            if resultado:
                datos_alumno = {
                    "Matrícula": resultado[0],
                    "Nombre": resultado[1],
                    "Apellido Paterno": resultado[2],
                    "Apellido Materno": resultado[3],
                    "Grupo": resultado[4],
                    "Semestre": resultado[5],
                }
                alumno_info(datos_alumno)
            else:
                messagebox.showerror("Error", f"No se encontró al alumno con matrícula {matricula}")

        except Exception as e:
            messagebox.showerror("Error de Base de Datos", str(e))
        finally:
            cursor.close()

    root = tk.Tk()
    root.title("Portal de Alumnos")
    root.geometry("400x300")

    tk.Label(root, text="Portal de Alumnos", font=("Helvetica", 16)).pack(pady=10)
    tk.Label(root, text="Ingrese la matrícula del alumno:", font=("Helvetica", 12)).pack(pady=5)
    entry_matricula = tk.Entry(root)
    entry_matricula.pack(pady=10)

    tk.Button(root, text="Buscar", command=obtener_datos_alumno).pack(pady=10)

    root.mainloop()
