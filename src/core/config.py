import os
from dotenv import load_dotenv

# Carrega variáveis de ambiente do arquivo .env se ele existir
load_dotenv()

class Settings:
    PROJECT_NAME: str = "Plataforma de Otimização de Portfólio HNWI"
    PROJECT_VERSION: str = "0.1.0"

    POSTGRES_USER: str = os.getenv("POSTGRES_USER", "postgres")
    POSTGRES_PASSWORD: str = os.getenv("POSTGRES_PASSWORD", "password")
    POSTGRES_SERVER: str = os.getenv("POSTGRES_SERVER", "localhost")
    POSTGRES_PORT: str = os.getenv("POSTGRES_PORT", "5432")
    POSTGRES_DB: str = os.getenv("POSTGRES_DB", "portfolio_optimization_db")
    
    DATABASE_URL: str = (
        f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@"
        f"{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"
    )

    # Configurações de Segurança para JWT
    SECRET_KEY: str = os.getenv("SECRET_KEY", "a_very_secret_key_please_change_in_production_environment")
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "30"))

    # Futuras configurações (e.g., segredos da API, etc.) podem ser adicionadas aqui
    API_V1_STR: str = "/api/v1"

settings = Settings()

# Para testar se está carregando:
# if __name__ == "__main__":
#     print(f"Database URL: {settings.DATABASE_URL}")
#     print(f"DB User: {settings.POSTGRES_USER}") # Para verificar se o .env está sendo lido 