from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.core.config import settings
# Import Base from your models file if you want to create tables from here
# from src.core.models import Base 

engine = create_engine(settings.DATABASE_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    """Dependency to get a database session."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Função para criar tabelas (chamar seletivamente, e.g., em um script de inicialização)
# def create_db_tables():
#     # Importar todos os modelos aqui para que sejam registrados no Base.metadata
#     # from src.core import models # Isso garante que todos os modelos sejam carregados
#     print(f"Creating tables for database at {settings.DATABASE_URL}")
#     Base.metadata.create_all(bind=engine)
#     print("Tables created (if they didn't exist).")

# if __name__ == "__main__":
#     print("Creating database tables...")
#     # Para executar isso, você precisaria garantir que todos os seus modelos
#     # sejam importados de alguma forma para que Base.metadata os conheça.
#     # Descomente a linha `from src.core.models import Base` no topo
#     # e a linha `from src.core import models` em `create_db_tables`
#     # e então, a linha abaixo:
#     # create_db_tables() 