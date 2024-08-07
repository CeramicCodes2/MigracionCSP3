-- Crear el esquema para el registro de quejas
CREATE SCHEMA IF NOT EXISTS registro_de_quejas;

-- Crear la tabla de quejas
CREATE TABLE IF NOT EXISTS registro_de_quejas.quejas (
    id_queja SERIAL PRIMARY KEY,
    texto_queja TEXT NOT NULL,
    email_quejoso VARCHAR(255) NOT NULL,
    nombres_personal_corrupto TEXT[]
);

-- Crear la tabla de dependencias
CREATE TABLE IF NOT EXISTS registro_de_quejas.dependencias (
    id_dependencia SERIAL PRIMARY KEY,
    nombre_dependencia VARCHAR(50) NOT NULL CHECK (nombre_dependencia IN ('AGE', 'CECTI', 'AGCTI', 'ACCT'))
);

-- Crear la tabla catálogo de estados de la queja
CREATE TABLE IF NOT EXISTS registro_de_quejas.estados_queja (
    id_estado SERIAL PRIMARY KEY,
    nombre_estado VARCHAR(50) NOT NULL CHECK (nombre_estado IN ('EN PROCESO DE REGISTRO', 'TURNADA', 'RETROALIMENTADA', 'RESUELTA'))
);

-- Crear la tabla para ligar dependencias y quejas con estados
CREATE TABLE IF NOT EXISTS registro_de_quejas.quejas_dependencias (
    id_queja INT REFERENCES registro_de_quejas.quejas(id_queja),
    id_dependencia INT REFERENCES registro_de_quejas.dependencias(id_dependencia),
    id_estado INT REFERENCES registro_de_quejas.estados_queja(id_estado),
    PRIMARY KEY (id_queja, id_dependencia)
);


