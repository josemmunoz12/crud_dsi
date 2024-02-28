from fastapi import APIRouter, HTTPException, Response, status
from app.api.config.db import conn
from app.api.models.user import users
from app.api.schemas.user import User
from typing import List
from sqlalchemy import select
from cryptography.fernet import Fernet

user = APIRouter()
key = Fernet.generate_key()
f = Fernet(key)

@user.get("/users", tags=["Facturas"], response_model=List[User], description="Obtener listas de factura")
def get_users():
    return conn.execute(users.select()).fetchall()

@user.get("/users/{id}", tags=["Facturas"], response_model=User, description="Obtener factura por ID")
def get_user(id: str):
    result = conn.execute(users.select().where(users.c.id == id)).first()
    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"la factura {id} no se encontro")
    return result

@user.post("/", tags=["Facturas"], response_model=User, description="Crear nueva factura")
def create_user(user: User):
    new_user = {"name": user.name, "descripcion": user.descripcion, "precio":user.precio}
    result = conn.execute(users.insert().values(new_user))
    created_user = conn.execute(users.select().where(users.c.id == result.lastrowid)).first()
    return created_user

@user.put("/users/{id}", tags=["Facturas"], description="Modificar factura Id")
def update_user(id: str, user: User):
    # Verificar si el usuario existe antes de actualizar
    existing_user = conn.execute(users.select().where(users.c.id == id)).first()
    if not existing_user:
        raise HTTPException(status_code=404, detail=f"la factura {id} no se encontro")
    
    conn.execute(users.update().values(name=user.name, descripcion=user.descripcion, 
                precio=user.precio).where(users.c.id==id))
    updated_user = conn.execute(users.select().where(users.c.id == id)).first()
    return {"message": "factura modificada", "user": updated_user}

@user.delete("/{id}", tags=["Facturas"], status_code=status.HTTP_204_NO_CONTENT, description="Eliminar la factura id")
def delete_user(id: str):
    existing_user = conn.execute(users.select().where(users.c.id == id)).first()
    if not existing_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"la factura {id} no se encontro")
    
    conn.execute(users.delete().where(users.c.id == id))
    return Response(status_code=status.HTTP_204_NO_CONTENT)
