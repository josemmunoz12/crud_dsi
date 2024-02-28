# CRUD API

## Estructura del Proyecto

. \
├── app \
│   ├── api \
│   │   ├── config \
│   │   │   ├── db.py  # Database configuration. \
│   │   ├── methods \
│   │   │   └── README.md  # Utility functions explanation for routes. \
│   │   ├── models \
│   │   │   └── user.py  # Pydantic models. \
│   │   └── routes \
│   │       └── user.py  # API routes. \
│   │   └── schema \
│   │       └── user.py  # schema request \
│   ├── app.py  # Entry point for the FastAPI application. \
└── .env.example \
└── Dockerfile \
└── README.md \
└── requirements.txt \

## Instrucciones de Configuración

1. **Configuración del entorno**: Asegúrese de tener Python 3.11.1 o superior instalado.
2. **Instalación de dependencias**: Ejecute `pip install -r requirements.txt` para instalar las dependencias necesarias.
3. **Variables de entorno**: Configure las variables de entorno necesarias como se describe en `app/` crear un archivo llamado `variables.env` teniendo encuenta la estructura de .env.example \ 
4. **Ejecución**: Ejecute `uvicorn app.app:app --reload` para iniciar el servidor de desarrollo en el puerto 8000.

## Instrucciones de ejecucion con el contenedor de DOCKER
1. Ejecute primero: "docker image build -t api" .
2. ejecute: "docker container run --publish 8080:80 api"
   

## Endpoints

El proyecto proporciona una serie de endpoints para realizar operaciones CRUD en `items`:

- `POST /`: Crea una nuevo factura.
- `GET /users/`: Lista todos las facturas.
- `GET /users/{id}/`: Obtiene una factura específico por ID.
- `PUT /users/{id}/`: Actualiza una factura específico por ID.
- `DELETE /users/{id}/`: Elimina una factura específico por ID.

## estructura table mysql 

"id", Integer, primary_key=True,
"name",String(255),
"descripcion", String(255),
"precio", Integer

## Licencia

Este proyecto está bajo la licencia de código abierto.
