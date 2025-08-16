# API LLM CV

API con LLM para análisis y procesamiento de CV usando FastAPI.

## 🚀 Características

- **FastAPI** - Framework web moderno y rápido
- **Endpoints LLM** - Generación de texto y análisis de CV
- **Documentación automática** - Swagger UI integrado
- **Multiplataforma** - Compatible con macOS, Windows y Linux

## 📋 Requisitos Previos

### Python
- **Python 3.8+** (recomendado Python 3.11+)

### Verificar instalación
```bash
# macOS/Linux
python3 --version

# Windows
python --version
```

## 🛠️ Instalación

### 1. Clonar el repositorio
```bash
git clone <tu-repositorio>
cd api-llm-cv
```

### 2. Crear entorno virtual (recomendado)

#### macOS/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

#### Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Instalar dependencias
```bash
# macOS/Linux
python3 -m pip install "fastapi[standard]"

# Windows
python -m pip install "fastapi[standard]"
```

## 🚀 Ejecución

### 1. Activar entorno virtual (si lo creaste)

#### macOS/Linux:
```bash
source venv/bin/activate
```

#### Windows:
```bash
venv\Scripts\activate
```

### 2. Ejecutar el servidor

#### macOS/Linux:
```bash
python3 -m uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

#### Windows:
```bash
python -m uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### 3. Acceder a la API
- **API principal**: http://localhost:8000
- **Documentación**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## 📚 Endpoints Disponibles

### LLM API
- `POST /api/llm/generate` - Generar texto con LLM
- `GET /api/llm/models` - Listar modelos disponibles
- `GET /api/llm/health` - Estado de la API

### Ejemplos de uso

#### Generar texto:
```bash
curl -X POST "http://localhost:8000/api/llm/generate" \
     -H "Content-Type: application/json" \
     -d '{"prompt": "Analiza este CV", "model": "default"}'
```

#### Ver modelos disponibles:
```bash
curl http://localhost:8000/api/llm/models
```

## 🔧 Desarrollo

### Estructura del proyecto
```
api-llm-cv/
├── main.py              # Aplicación principal
├── src/
│   ├── api/
│   │   └── llm/
│   │       └── routes.py  # Rutas de la API
│   └── __init__.py
└── README.md
```

### Modo desarrollo
El servidor se ejecuta con `--reload`, por lo que se reiniciará automáticamente cuando modifiques el código.

## 🌐 Acceso desde otros dispositivos

Si quieres acceder desde otros dispositivos en tu red local:
```bash
# macOS/Linux
python3 -m uvicorn main:app --reload --host 0.0.0.0 --port 8000

# Windows
python -m uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

Luego accede desde: `http://[TU-IP-LOCAL]:8000`

## 🐛 Solución de problemas

### Error: "command not found: python"
- **macOS**: Usa `python3` en lugar de `python`
- **Windows**: Asegúrate de que Python esté en el PATH
- **Linux**: Instala Python con `sudo apt install python3` (Ubuntu/Debian)

### Error: "command not found: pip"
- **macOS/Linux**: Usa `python3 -m pip`
- **Windows**: Usa `python -m pip`

### Puerto 8000 ocupado
Cambia el puerto:
```bash
python3 -m uvicorn main:app --reload --port 8001
```

## 📝 Licencia

Este proyecto es de uso personal para análisis de CV.
