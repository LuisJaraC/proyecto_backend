## Proyecto drf

Aplicación web y API REST para la gestión de tickets de soporte desarrollada con Django y Django REST Framework.

## Requisitos Previos

* Python 3.10 o superior
* `pip` (gestor de paquetes de Python)
* PostgreSQL instalado y ejecutándose localmente

## Instalación y ejecución

### 1. Clonar repositorio
```bash
git clone [https://github.com/LuisJaraC/proyecto_backend.git](https://github.com/LuisJaraC/proyecto_backend.git)
cd proyecto_backend
```

### 2. Crear un entorno virtual (dentro de la carpeta del proyecto)

En **Windows**:
```bash
python -m venv venv
```

En **Linux / macOS**:
```bash
python3 -m venv venv
```

### 3. Activar el entorno virtual

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

### 4. Instalar las dependencias
```bash
pip install -r requirements.txt
```

### 5. Configurar la base de datos (PostgreSQL)

En **Windows (o pgAdmin)**:
```bash
psql -U postgres
```

En **Linux / macOS**:
```bash
sudo -u postgres psql
```
Y configura tu base de datos asignando los permisos necesarios...

### 6. Configurar variables de entorno
Crea un archivo llamado `.env` dentro de la carpeta raíz del proyecto (junto a `manage.py`) y asigna las variables de entorno.


### 7. Ejecutar las migraciones y crear el superusuario
```bash
python manage.py makemigrations tickets
python manage.py migrate
python manage.py createsuperuser
```

### 8. Levantar el servidor
```bash
python manage.py runserver
```

Abre [http://127.0.0.1:8000](http://127.0.0.1:8000) en tu navegador.

## Rutas y Endpoints Disponibles

### Vistas Web y Autenticación
* **Vista Pública de Bienvenida:** [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
* **Inicio de Sesión (Login):** [http://127.0.0.1:8000/login/](http://127.0.0.1:8000/login/)
* **Vista Protegida por Función (FBV):** [http://127.0.0.1:8000/dashboard-por-funcion/](http://127.0.0.1:8000/dashboard-por-funcion/)
* **Vista Protegida por Clase (CBV):** [http://127.0.0.1:8000/panel-por-clase/](http://127.0.0.1:8000/panel-por-clase/)
* **Panel de Administración:** [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

### Endpoints de la API REST
* **Tickets (CRUD):** [http://127.0.0.1:8000/api/tickets/](http://127.0.0.1:8000/api/tickets/)
* **Historial (CRUD):** [http://127.0.0.1:8000/api/historial/](http://127.0.0.1:8000/api/historial/)