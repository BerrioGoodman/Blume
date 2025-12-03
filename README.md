# Blume

Blume es una API REST completa de Django diseñada para gestionar una plataforma de aplicaciones de empleo. Facilita conexiones entre estudiantes, empresas e instituciones educativas proporcionando herramientas para publicar vacantes de empleo, enviar aplicaciones y rastrear estadísticas.

## Arquitectura

Blume sigue una arquitectura modular de Django con múltiples aplicaciones especializadas:

- **Core**: Configuración principal del proyecto Django y ajustes
- **Students**: Gestiona perfiles de estudiantes y su información académica
- **Companies**: Maneja registros de empresas y detalles comerciales
- **Vacancies**: Gestiona ofertas de trabajo creadas por empresas
- **Application Jobs**: Procesa y rastrea aplicaciones de trabajo de estudiantes a vacantes
- **Administrator**: Gestiona usuarios administrativos y controles de acceso
- **Teacher**: Maneja perfiles de profesores e información departamental
- **Stats**: Proporciona datos estadísticos y análisis

La arquitectura utiliza el modelo User incorporado de Django como base, con relaciones OneToOne extendiendo perfiles de usuario para diferentes roles.

## Tecnologías Utilizadas

- **Framework Backend**: Django 5.0+
- **Framework API**: Django REST Framework (DRF) 3.14+
- **Base de Datos**: PostgreSQL
- **Autenticación**: JWT (JSON Web Tokens) con django-rest-framework-simplejwt
- **CORS**: django-cors-headers para solicitudes de origen cruzado
- **Documentación API**: drf-spectacular (Swagger/OpenAPI)
- **Gestión de Entorno**: python-decouple
- **Controlador de Base de Datos**: psycopg2-binary

## Características

### Gestión de Usuarios
- Autenticación basada en roles (Estudiantes, Empresas, Profesores, Administradores)
- Autenticación basada en tokens JWT
- Registro y login de usuarios seguros

### Características para Estudiantes
- Gestión de perfil con información de carrera y semestre
- Envío de aplicaciones de trabajo
- Seguimiento del estado de aplicaciones

### Características para Empresas
- Gestión de perfil de empresa
- Creación y gestión de vacantes de trabajo
- Revisión y gestión de aplicaciones

### Gestión de Empleos
- Publicación de vacantes con requisitos detallados
- Información salarial
- Seguimiento de fecha de publicación
- Recolección de aplicaciones y actualizaciones de estado

### Características Administrativas
- Gestión de roles de usuario
- Controles de nivel de acceso
- Estadísticas y análisis del sistema

### Análisis
- Recuentos totales de estudiantes, empresas, vacantes y aplicaciones
- Estadísticas de estado de aplicaciones (aceptadas/rechazadas)

## Instalación

### Prerrequisitos
- Python 3.8 o superior
- Base de datos PostgreSQL
- Git

### Clonar el Repositorio
```bash
git clone <url-del-repositorio>
cd Blume
```

### Crear Entorno Virtual
```bash
python -m venv venv
# En Windows
venv\Scripts\activate
# En macOS/Linux
source venv/bin/activate
```

### Instalar Dependencias
```bash
cd backend
pip install -r requirements.txt
```

## Configuración

### Variables de Entorno
Crea un archivo `.env` en el directorio `backend/` con las siguientes variables:

```env
DB_NAME=tu_nombre_de_base_de_datos
DB_USER=tu_usuario_de_base_de_datos
DB_PASSWORD=tu_contraseña_de_base_de_datos
DB_HOST=localhost
DB_PORT=5432
```

### Configuración de Base de Datos
1. Crea una base de datos PostgreSQL
2. Ejecuta las migraciones:
```bash
python manage.py makemigrations
python manage.py migrate
```

### Crear Superusuario (Opcional)
```bash
python manage.py createsuperuser
```

## Uso

### Ejecutar el Servidor de Desarrollo
```bash
python manage.py runserver
```

La API estará disponible en `http://127.0.0.1:8000/`

### Documentación de la API
- Swagger UI: `http://127.0.0.1:8000/api/`
- ReDoc: `http://127.0.0.1:8000/api/schema/redoc/`
- Esquema OpenAPI: `http://127.0.0.1:8000/api/schema/`

### Autenticación
Obtén tokens JWT:
```bash
POST /api/token/
{
  "username": "tu_usuario",
  "password": "tu_contraseña"
}
```

Usa el token de acceso en el encabezado Authorization:
```
Authorization: Bearer <token_de_acceso>
```

Refresca tokens:
```bash
POST /api/token/refresh/
{
  "refresh": "tu_token_de_refresh"
}
```

## Endpoints de la API

### Autenticación
- `POST /api/token/` - Obtener par de tokens JWT
- `POST /api/token/refresh/` - Refrescar token de acceso

### Estudiantes
- `GET/POST /estudiantes/` - Listar/Crear estudiantes
- `GET/PUT/PATCH/DELETE /estudiantes/{id}/` - Detalle de estudiante

### Empresas
- `GET/POST /empresas/` - Listar/Crear empresas
- `GET/PUT/PATCH/DELETE /empresas/{id}/` - Detalle de empresa

### Vacantes
- `GET/POST /vacantes/` - Listar/Crear vacantes
- `GET/PUT/PATCH/DELETE /vacantes/{id}/` - Detalle de vacante

### Aplicaciones
- `GET/POST /postulaciones/` - Listar/Crear aplicaciones
- `GET/PUT/PATCH/DELETE /postulaciones/{id}/` - Detalle de aplicación

### Administradores
- `GET/POST /administradores/` - Listar/Crear administradores
- `GET/PUT/PATCH/DELETE /administradores/{id}/` - Detalle de administrador

### Profesores
- `GET/POST /docentes/` - Listar/Crear profesores
- `GET/PUT/PATCH/DELETE /docentes/{id}/` - Detalle de profesor

### Estadísticas
- Endpoints de estadísticas disponibles a través de la aplicación stats

## Modelos de Datos

### Usuario (incorporado en Django)
- username, email, password, etc.

### Estudiante (EstudianteModel)
- user (OneToOneField a User)
- carrera (carrera)
- semestre (semestre)

### Empresa (companyModel)
- user (OneToOneField a User)
- nombre_empresa (nombre de empresa)
- sector_industria (sector industrial)
- direccion (dirección)
- telefono (teléfono)

### Vacante
- company (ForeignKey a companyModel)
- titulo (título)
- descripcion (descripción)
- requisitos (requisitos)
- fecha_publicacion (fecha de publicación)
- salario (salario)

### Aplicación (ApplicationJobModel)
- estudiante (ForeignKey a EstudianteModel)
- vacante (ForeignKey a Vacancy)
- estado (estado: pendiente, aceptado, rechazado)
- fecha_postulacion (fecha de aplicación)

### Profesor
- user (OneToOneField a User)
- materia (materia)
- departamento (departamento)

### Administrador (AministratorModel)
- user (OneToOneField a User)
- rol (rol)
- nivel_acceso (nivel de acceso)

### Estadísticas (StatisticsModel)
- total_students
- total_companies
- total_vacancies
- total_applications
- total_accepted_applications
- total_rejected_applications

## Contribución

1. Haz fork del repositorio
2. Crea una rama de funcionalidad
3. Realiza tus cambios
4. Agrega pruebas si corresponde
5. Envía un pull request

Por favor sigue la plantilla de pull request en `.github/PULL_REQUEST_TEMPLATE.md`
