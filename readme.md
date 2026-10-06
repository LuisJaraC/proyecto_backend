## Proyecto drf

Aplicación web con Django.

## Requisitos Previos

* Python 3.10 o superior
* `pip` (gestor de paquetes de Python)

## Instalación y ejecución
**1. Clonar repositorio**
```bash
git clone https://github.com/LuisJaraC/proyecto_backend.git
cd proyecto_backend

**2. Crear un entorno virtual** (dentro de la carpeta del proyecto)

En **Windows**:
```bash
python -m venv venv
```

En **Linux / macOS**:
```bash
python3 -m venv venv
```

**3. Activar el entorno virtual**

En **Windows (CMD)**:
```bash
venv\Scripts\activate
```

En **Windows (PowerShell)**:
```bash
venv\Scripts\Activate.ps1
```

En **Linux / macOS**:
```bash
source venv/bin/activate
```

**4. Instalar las dependencias**
```bash
pip install -r requirements.txt
```

**5. Ejecutar las migraciones**
```bash
python manage.py migrate
```

**6. Configurar la base de datos**
En **Windows (o Pgadmin)**:
```bash
psql -U postgres
```
En **Linux o MacOS**:
```bash
sudo -u postgres psql
```
**Una vez dentro, ejecuta los siguientes comandos para crear la base de datos y asignar permisos:**
SQL

CREATE DATABASE tickets_db;
CREATE USER tickets_admin WITH PASSWORD 'admin_password123';
ALTER ROLE tickets_admin SET client_encoding TO 'utf8';
ALTER ROLE tickets_admin SET default_transaction_isolation TO 'read committed';
ALTER ROLE tickets_admin SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE tickets_db TO tickets_admin;
\c tickets_db
GRANT ALL ON SCHEMA public TO tickets_admin;
\q

**7. Configurar variables de entorno**
Crear un archivo .env con las variables dentro de la carpeta raiz del proyecto.

**8. Ejecuta las migraciones y crea el superusuario**
```bash
python manage.py makemigrations tickets
python manage.py migrate
python manage.py createsuperuser
```
**9. Levanta el servidor**
```bash
python manage.py runserver
```


Abre [http://127.0.0.1:8000](http://127.0.0.1:8000) en tu navegador.

**ENDPOINTS DE LA API**
*Panel de Administración: http://127.0.0.1:8000/admin/*

*Tickets (CRUD): http://127.0.0.1:8000/api/tickets/*

*Historial (CRUD): http://127.0.0.1:8000/api/historial/*