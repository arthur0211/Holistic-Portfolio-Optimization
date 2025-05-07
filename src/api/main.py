from fastapi import FastAPI

from src.core.config import settings
from src.api.endpoints import client_profiles, login, users # Importa os novos routers

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.PROJECT_VERSION,
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

# Roteador principal para a v1 da API
api_router_v1 = FastAPI(title=f"{settings.PROJECT_NAME} v1", version="1.0")

@api_router_v1.get("/")
async def read_api_v1_root() -> dict[str, str]:
    return {"message": f"Bem-vindo à API v1 da {settings.PROJECT_NAME}!"}

# Inclui os routers específicos
api_router_v1.include_router(login.router, prefix="/login", tags=["Login"])
api_router_v1.include_router(users.router, prefix="/users", tags=["Users"])
api_router_v1.include_router(client_profiles.router, prefix="/clients", tags=["Client Profiles"])

# Monta o roteador da v1 na aplicação principal
app.mount(settings.API_V1_STR, api_router_v1)


@app.get("/")
async def read_root() -> dict[str, str]:
    """Endpoint raiz da aplicação."""
    return {"message": f"Bem-vindo à {settings.PROJECT_NAME}! Acesse {settings.API_V1_STR}/docs para a documentação da API."}

# Adicionar outros endpoints e lógica da API aqui conforme o desenvolvimento.
