import uuid
from typing import Any, Dict, Optional, Union, List

from sqlalchemy.orm import Session

from src.core.models import User
from src.api.schemas.user import UserCreate, UserUpdate
from src.core.security import get_password_hash, verify_password

# Funções CRUD para o modelo User

def get_user(db: Session, user_id: uuid.UUID) -> Optional[User]:
    """Busca um usuário pelo ID."""
    return db.query(User).filter(User.id == user_id).first()

def get_user_by_email(db: Session, email: str) -> Optional[User]:
    """Busca um usuário pelo email."""
    return db.query(User).filter(User.email == email).first()

def get_users(db: Session, skip: int = 0, limit: int = 100) -> List[User]:
    """Busca uma lista de usuários com paginação."""
    return db.query(User).offset(skip).limit(limit).all()

def create_user(db: Session, *, obj_in: UserCreate) -> User:
    """Cria um novo usuário."""
    hashed_password = get_password_hash(obj_in.password)
    db_obj = User(
        email=obj_in.email,
        hashed_password=hashed_password,
        full_name=obj_in.full_name,
        is_active=obj_in.is_active if obj_in.is_active is not None else True,
        # is_superuser=obj_in.is_superuser # Se tivermos superusuários
    )
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def update_user(
    db: Session, *, db_obj: User, obj_in: Union[UserUpdate, Dict[str, Any]]
) -> User:
    """Atualiza um usuário existente."""
    if isinstance(obj_in, dict):
        update_data = obj_in
    else:
        update_data = obj_in.model_dump(exclude_unset=True)

    if "password" in update_data and update_data["password"]:
        hashed_password = get_password_hash(update_data["password"])
        del update_data["password"] # Remove senha em texto plano dos dados de atualização
        update_data["hashed_password"] = hashed_password
    
    for field in update_data:
        if hasattr(db_obj, field):
            setattr(db_obj, field, update_data[field])
    
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def authenticate_user(db: Session, email: str, password: str) -> Optional[User]:
    """Autentica um usuário. Retorna o usuário se as credenciais forem válidas, senão None."""
    user = get_user_by_email(db, email=email)
    if not user:
        return None
    if not verify_password(password, user.hashed_password):
        return None
    return user

def is_user_active(user: User) -> bool:
    """Verifica se um usuário está ativo."""
    return user.is_active

# def is_superuser(user: User) -> bool:
#     """Verifica se um usuário é superusuário."""
#     return user.is_superuser

# Não vamos implementar delete de usuário por enquanto, apenas desativação (is_active=False)
# def remove_user(db: Session, *, user_id: uuid.UUID) -> Optional[User]:
#     obj = db.query(User).get(user_id)
#     if obj:
#         db.delete(obj)
#         db.commit()
#     return obj 