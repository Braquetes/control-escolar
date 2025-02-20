CREATE DATABASE control_escolar;

USE control_escolar;

-- Tabla para alumnos
CREATE TABLE alumnos (
    matricula VARCHAR(15) PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    apellido_paterno VARCHAR(50) NOT NULL,
    apellido_materno VARCHAR(50),
    grupo VARCHAR(10) NOT NULL,
    semestre INT NOT NULL
);

-- Tabla para calificaciones
CREATE TABLE calificaciones (
    id INT AUTO_INCREMENT PRIMARY KEY,
    matricula VARCHAR(15) NOT NULL,
    materia VARCHAR(50) NOT NULL,
    calificacion DECIMAL(5, 2) NOT NULL,
    semestre INT NOT NULL,
    FOREIGN KEY (matricula) REFERENCES alumnos(matricula) ON DELETE CASCADE
);

-- Tabla para administradores
CREATE TABLE administradores (
    usuario VARCHAR(50) PRIMARY KEY,
    contrasena VARCHAR(255) NOT NULL
);
