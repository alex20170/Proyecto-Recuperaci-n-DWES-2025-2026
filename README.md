# Proyecto Recetas

Una aplicación web Django para compartir, gestionar y descubrir recetas de cocina.

## Características

- 👥 **Sistema de Usuarios**: Registro e inicio de sesión
- 📝 **Gestión de Recetas**: Crear, editar y eliminar recetas
- 🏷️ **Categorización**: Organiza recetas por categorías
- 💬 **Comentarios**: Los usuarios pueden comentar en las recetas
- 🔍 **Búsqueda**: Encuentra recetas por título, autor o categoría
- 🔒 **Autenticación**: Solo usuarios registrados pueden crear recetas

## Requisitos

- Python 3.11+
- Django 5.2.10
- SQLite3 (incluido con Python)

## Instalación

1. **Clonar o descargar el proyecto**
   ```bash
   cd proyecto_recetas
   ```

2. **Crear un entorno virtual**
   ```bash
   python -m venv venv
   ```

3. **Activar el entorno virtual**
   - En Windows:
   ```bash
   venv\Scripts\activate
   ```
   - En macOS/Linux:
   ```bash
   source venv/bin/activate
   ```

4. **Instalar dependencias**
   ```bash
   pip install django
   ```

5. **Aplicar migraciones**
   ```bash
   python manage.py migrate
   ```

6. **Crear un superusuario (opcional)**
   ```bash
   python manage.py createsuperuser
   ```

## Uso

### Iniciar el servidor
```bash
python manage.py runserver
```

El servidor estará disponible en `http://127.0.0.1:8000/`

### Rutas principales

- **Inicio**: `/` - Lista de todas las recetas
- **Registrarse**: `/registrar/` - Crear una nueva cuenta
- **Iniciar sesión**: `/accounts/login/` - Acceder con cuenta existente
- **Crear receta**: `/receta/nueva/` - Agregar una nueva receta (requiere login)
- **Detalle de receta**: `/receta/<id>/` - Ver detalles y comentarios
- **Editar receta**: `/receta/<id>/editar/` - Modificar receta propia
- **Eliminar receta**: `/receta/<id>/eliminar/` - Borrar receta propia
- **Admin**: `/admin/` - Panel de administración

## Estructura del Proyecto

```
proyecto_recetas/
├── proyecto_recetas/     # Configuración del proyecto
│   ├── settings.py       # Configuración general
│   ├── urls.py          # URLs principales
│   ├── wsgi.py          # Configuración WSGI
│   └── asgi.py          # Configuración ASGI
├── recetas/              # Aplicación principal
│   ├── models.py        # Modelos (Receta, Categoría, Comentario)
│   ├── views.py         # Vistas (lógica de negocio)
│   ├── forms.py         # Formularios (incluyendo RegistroForm)
│   ├── urls.py          # URLs de la app
│   ├── templates/       # Plantillas HTML
│   └── static/          # Archivos estáticos (CSS, JS)
├── manage.py            # Herramienta de gestión Django
└── db.sqlite3           # Base de datos SQLite

```

## Funcionalidades principales

### 1. Registro de usuarios
- Los usuarios nuevos pueden registrarse creando un username, email y contraseña
- Las contraseñas se validan automáticamente
- Los emails duplicados se rechazan

### 2. Autenticación
- Login seguro con contraseña
- Cierre de sesión
- Redirección automática después de registrarse

### 3. Gestión de recetas
- Crear recetas con: título, ingredientes, pasos, tiempo de preparación y categoría
- Solo el autor puede editar o eliminar sus recetas
- Ver todas las recetas públicamente

### 4. Búsqueda y filtros
- Buscar por título de receta
- Buscar por autor
- Filtrar por categoría

### 5. Sistema de comentarios
- Usuarios autenticados pueden comentar en recetas
- Ver comentarios en el detalle de la receta

## Modelos de Base de Datos

### Usuarios (Django Auth)
- username
- email
- password (hasheada)

### Receta
- título
- ingredientes (texto)
- pasos (texto)
- tiempo_preparacion (minutos)
- categoría (FK)
- autor (FK a User)
- fecha_creación

### Categoría
- nombre
- descripción

### Comentario
- contenido
- autor (FK a User)
- receta (FK a Receta)
- fecha_creación

## Contribución

Para agregar nuevas características:

1. Crear una rama para tu feature
2. Hacer cambios en el código
3. Probar localmente
4. Hacer commit de los cambios

## Licencia

Este proyecto es de código abierto.

## Soporte

Para problemas o preguntas, contacta al equipo de desarrollo.

---

**Última actualización**: 31 de mayo de 2026
