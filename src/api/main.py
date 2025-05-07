from fastapi import FastAPI

app = FastAPI(
    title="Plataforma de Otimização de Portfólio HNWI",
    description="API para a plataforma de otimização de portfólio HNWI focada no mercado brasileiro.",
    version="0.1.0",
)


@app.get("/")
async def read_root() -> dict[str, str]:
    """Endpoint raiz da aplicação."""
    return {"message": "Bem-vindo à API de Otimização de Portfólio HNWI!"}


# Adicionar outros endpoints e lógica da API aqui conforme o desenvolvimento.
