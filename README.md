# 📦 Mini Distribuidora

Aplicación **Django** para la gestión logística de una mini distribuidora.  
Permite administrar clientes, albaranes y líneas de producto de forma sencilla mediante una interfaz web.

---

## 🧩 Funcionalidades

- Gestión de **clientes**
- Creación y edición de **albaranes**
- Gestión de **líneas de producto** asociadas a cada albarán
- Control de **estados**
- Vistas detalladas para consulta de información

---

## 🛠️ Tecnologías utilizadas

- Python 3
- Django
- SQLite (base de datos por defecto)
- HTML / CSS

---

## 🚀 Instalación y uso

### 1️⃣ Clonar el repositorio
```bash
git clone https://github.com/albaboo/mini_distribuidora.git
cd mini_distribuidora
```

### 2️⃣ Crear y activar entorno virtual
```bash
python -m venv venv
source venv/bin/activate  # Linux / Mac
venv\Scripts\activate     # Windows
```

### 3️⃣ Instalar dependencias
```bash
pip install -r requirements.txt
```

### 4️⃣ Aplicar migraciones
```bash
python manage.py migrate
```

### 5️⃣ Ejecutar el servidor
```bash
python manage.py runserver
```

Accede desde el navegador a:  
👉 `http://127.0.0.1:8000/`

---

## 📁 Estructura del proyecto

```
mini_distribuidora/
├── mp_app/                 # Aplicación principal
├── mini_distribuidora/     # Configuración del proyecto
├── templates/              # Plantillas HTML
├── manage.py
├── db.sqlite3
├── requirements.txt
└── .gitignore
```

---

## 📄 Licencia

Este proyecto se distribuye bajo la licencia **MIT**.  
Puedes usarlo, modificarlo y adaptarlo libremente.

---

## ✨ Autor

Desarrollado por **albaboo**  
Proyecto educativo / práctico para gestión básica de distribuidoras.

---


More info [here](https://deepwiki.com/albaboo/mini_distribuidora)

