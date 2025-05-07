from fastapi.testclient import TestClient

from src.api.main import app

client = TestClient(app)


def test_read_root() -> None:
    """Testa o endpoint raiz."""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {
        "message": "Bem-vindo à API de Otimização de Portfólio HNWI!"
    }
