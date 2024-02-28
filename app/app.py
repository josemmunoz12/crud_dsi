from fastapi import FastAPI
from app.api.routes.user import user


app = FastAPI(
    title="Facturas API",
    description="a REST API using python and mysql",
    version="0.0.1",
    openapi_tags=[{
    "name": "Facturas",
    "description": "Facturas endpoint"
  }]
)

app.include_router(user)