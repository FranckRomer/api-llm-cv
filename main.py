from typing import Union
from fastapi import FastAPI
from src.api.routes import api_router

app = FastAPI(
    title="API LLM CV",
    description="API para procesamiento de lenguaje natural y análisis de CV",
    version="1.0.0"
)

# Incluir todas las rutas de la API de manera centralizada
app.include_router(api_router)

@app.get("/")
def read_root():
    return {"Hello": "World", "service": "API LLM CV"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}