from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional, List

# Crear el router para las rutas de LLM
router = APIRouter(prefix="/api/llm", tags=["LLM"])

# Modelos de datos
class LLMRequest(BaseModel):
    prompt: str
    model: Optional[str] = "default"
    max_tokens: Optional[int] = 1000
    temperature: Optional[float] = 0.7

class LLMResponse(BaseModel):
    response: str
    model: str
    tokens_used: int
    status: str

# Endpoint principal para generar texto
@router.post("/generate", response_model=LLMResponse)
async def generate_text(request: LLMRequest):
    """
    Genera texto usando un modelo de lenguaje
    """
    try:
        # Aquí irá la lógica de generación con el LLM
        # Por ahora retornamos una respuesta de ejemplo
        return LLMResponse(
            response=f"Respuesta generada para: {request.prompt}",
            model=request.model,
            tokens_used=len(request.prompt.split()),
            status="success"
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Endpoint para obtener información del modelo
@router.get("/models")
async def get_models():
    """
    Retorna la lista de modelos disponibles
    """
    return {
        "models": [
            {"id": "default", "name": "Modelo por defecto", "type": "text-generation"},
            {"id": "gpt-3.5", "name": "GPT-3.5", "type": "text-generation"},
            {"id": "gpt-4", "name": "GPT-4", "type": "text-generation"}
        ]
    }

# Endpoint de salud
@router.get("/health")
async def health_check():
    """
    Verifica el estado de la API
    """
    return {"status": "healthy", "service": "LLM API"}
