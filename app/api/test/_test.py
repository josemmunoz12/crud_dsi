import pytest
from fastapi.testclient import TestClient
from app.app import app 

client = TestClient(app)

@pytest.fixture
def generic_user():
    # Crear un usuario genérico utilizando el cliente de pruebas
    user_data = {
        "name": "Generic User",
        "descripcion": "Generic Description",
        "precio": 50
    }
    response = client.post("/", json=user_data)
    assert response.status_code == 200
    return response.json()

def test_get_users(generic_user):
    # Prueba para obtener la lista de usuarios
    response = client.get("/users")
    assert response.status_code == 200
  

def test_get_user(generic_user):
    # Prueba para obtener un usuario por su id
    user_id = generic_user['id']
    response = client.get(f"/users/{user_id}")
    assert response.status_code == 200
  

def test_update_user(generic_user):
    # Prueba para actualizar un usuario
    user_id = generic_user['id']
    updated_user_data = {"name": "Updated Name", "descripcion": "Updated Description", "precio": 100}
    response = client.put(f"/users/{user_id}", json=updated_user_data)
    assert response.status_code == 200
  

def test_delete_user(generic_user):
    # Prueba para eliminar un usuario
    user_id = generic_user['id']
    response = client.delete(f"/{user_id}")
    print(user_id)
    assert response.status_code == 204
  