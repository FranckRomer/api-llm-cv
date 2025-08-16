from fastapi import APIRouter
from src.api.llm.endpoints import router as llm_router

# Crear el router principal de la API
api_router = APIRouter(prefix="/api/v1")

# Incluir todas las rutas de los módulos
api_router.include_router(llm_router, tags=["LLM"])

# Aquí puedes agregar más módulos en el futuro:
# from src.api.cv.routes import router as cv_router
# api_router.include_router(cv_router, prefix="/cv", tags=["CV"])
# 
# from src.api.auth.routes import router as auth_router
# api_router.include_router(auth_router, prefix="/auth", tags=["Auth"]) 