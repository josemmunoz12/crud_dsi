from sqlalchemy import create_engine, MetaData
import os
from dotenv import load_dotenv


# Cargar variables de entorno
load_dotenv('app/variables.env')   # Asegúrate de especificar la ruta correcta a tu archivo .env si no está en el directorio actual

# Construir la cadena de conexión a partir de las variables de entorno
db_engine = os.getenv("DB_ENGINE")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
db_host = os.getenv("DB_HOST")
db_port = os.getenv("DB_PORT")
db_name = os.getenv("DB_NAME")

database_url = f"{db_engine}://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"

# Usar la cadena de conexión para crear el motor de base de datos
engine = create_engine(database_url)
meta = MetaData()
conn = engine.connect()
