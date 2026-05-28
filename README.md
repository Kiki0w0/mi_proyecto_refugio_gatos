# mi_proyecto_refugio_gatos

Alumna: Victoria Catalina Villarroel
Comisión: #89385
Curso: Python

Info sobre el proyecto:
Es una página para un refugio que rescata gatos llamado Gatitos de la Sarmiento. En el se podrán ver 
qué gatos del refugio están en adopción y hacer solicitudes de adopción.
Las solicitudes de adopción pueden ser administradas desde el panel correspondiente para fines demostrativos del CRUD requerido por la consigna.

## Funcionalidades

- Registro y login de usuarios
- CRUD de gatos
- CRUD de categorías
- CRUD de solicitudes de adopción
- Panel administrador de Django
- Búsqueda de gatos
- Página de inicio y navegación


El proyecto fué realizado con lenguaje Python (versión 3.14.5) y framework Django (versión 6.0.5). Lo visual fué realizado con bootstrap 5.

## Instalación:

Clonación del repositorio:
git clone URL_DEL_REPOSITORIO

Creación del entorno virtual:
python -m venv .venv

Activación del entorno virtual:
.venv\Scripts\activate

Instalación de dependencias:
pip install django

Aplicación de migraciones:
python manage.py migrate

Ejecución del servidor:
python manage.py runserver



## Acceso al administrador:
http://127.0.0.1:8000/admin

Crear SuperUsuario:
python manage.py createsuperuser


## Información sobre la página web y la página de la administración:

Categoría está pensada para separar a los gatos según grupo etario. Se podría agregar la categoría
gatito, la categoría adulto y la categoría adulto mayor. Se accede a través de http://127.0.0.1:8000/admin/

El botón Gatos que está en la ventana de bienvenida te lleva a crear Gatos. Acá podés anotar los datos del gato del refugio (grupo etario, nombre del gato, carácter en la descipción, edad, sexo y si está disponible para adoptar). También podés eliminar el perfil del gato o editarlo.

Para agregar una solicitud de adopción se ingresa a http://127.0.0.1:8000/admin/. Al añadir una solicitud de
adopción nueva podrás elegir el nombre del gato del cual se está interesado, el nombre del adoptante, la dirección del mail del adoptante y un mensaje comentando por qué quiere adoptar.

