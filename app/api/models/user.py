from sqlalchemy import Column, Table
from sqlalchemy.sql.sqltypes import Integer, String
from app.api.config.db import meta, engine

users = Table(
    "Recibo",
    meta,
    Column("id", Integer, primary_key=True),
    Column("name",String(255)),
    Column("descripcion", String(255)),
    Column("precio", Integer),
)

meta.create_all(engine)
