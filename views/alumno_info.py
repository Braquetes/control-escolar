import tkinter as tk

def alumno_info(datos_alumno):
    """
    Mostrar la información del alumno en una ventana nueva.

    :param datos_alumno: Diccionario con los datos del alumno.
    """
    info_window = tk.Toplevel()
    info_window.title("Información del Alumno")
    info_window.geometry("400x300")

    tk.Label(info_window, text="Información del Alumno", font=("Helvetica", 16)).pack(pady=10)

    for campo, valor in datos_alumno.items():
        texto = f"{campo} - {valor}"
        tk.Label(info_window, text=texto, font=("Helvetica", 12)).pack(pady=5)

    tk.Button(info_window, text="Cerrar", command=info_window.destroy).pack(pady=20)
