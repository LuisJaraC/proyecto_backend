-- 1. Crear base de datos
CREATE DATABASE tickets_db;

-- 2. Crear usuario
CREATE USER tickets_admin WITH PASSWORD 'admin_password123';

-- 3. Asignar permisos 
ALTER ROLE tickets_admin SET client_encoding TO 'utf8';
ALTER ROLE tickets_admin SET default_transaction_isolation TO 'read committed';
ALTER ROLE tickets_admin SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE tickets_db TO tickets_admin;