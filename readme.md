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
pip install django
```

**5. Ejecutar las migraciones**
```bash
python manage.py migrate
```

**6. Levantar el servidor**
```bash
python manage.py runserver
```

Abre [http://127.0.0.1:8000](http://127.0.0.1:8000) en tu navegador.
