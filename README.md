# Flask + PostgreSQL + Docker Compose

Este proyecto es una API simple para gestionar estudiantes (CRUD) utilizando Flask, PostgreSQL y Docker Compose.

## Requisitos

- Docker
- Docker Compose
- Tener libre el puerto 5000 de localhost
- Tener espacio suficiente en disco
- Tener una distribución de linux Ubuntu/Debian

## Estructura del Proyecto

docker-compose-db/  
│  
├── docker-compose.yml  
├── app/  
│ ├── Dockerfile  
│ ├── requirements.txt  
│ ├── app.py  
│ └── models.py  
└── db/  
└── init.sq


## Pasos para Ejecutar el Proyecto

1. **Clona el repositorio:**

   `git clone https://github.com/julianReyes-dev/docker-compose-db.git`  
   `cd docker-compose-db`

3. **Levanta los servicios con Docker Compose:**

   `export COMPOSE_HTTP_TIMEOUT=240`  
   `docker-compose up --build`

   > "export COMPOSE_HTTP_TIMEOUT=240" se hace con el fin de que si en cualquier caso de que la construcción de los contenedores se demora demasiado, la base de datos no se cierre por timeout.

5. **Prueba la API:**

   **Crear un estudiante:**  
   `curl -X POST -H "Content-Type: application/json" -d '{"nombre": "Juan", "edad": 22, "carrera": "Ingeniería"}' http://localhost:5000/students`

   **Obtener todos los estudiantes:**  
   `curl http://localhost:5000/students`

   **Obtener un estudiante por ID:**  
   `curl http://localhost:5000/students/1`

   **Actualizar un estudiante:**  
   `curl -X PUT -H "Content-Type: application/json" -d '{"nombre": "Juan Perez", "edad": 23, "carrera": "Ingeniería Civil"}' http://localhost:5000/students/1`

   **Eliminar un estudiante:**  
   `curl -X DELETE http://localhost:5000/students/1`

7. **Detener los contenedores:**

   `docker-compose down`

## Tecnologías Utilizadas

**Flask:** Framework web para crear la API.  
**PostgreSQL:** Base de datos para almacenar la información de los estudiantes.  
**Docker:** Para contenerizar la aplicación y la base de datos.  
**Docker Compose:** Para orquestar los servicios.
