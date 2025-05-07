from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from src.api import schemas
from src.core import crud
from src.db.session import get_db
# from src.api.dependencies import get_current_active_superuser # Para proteger no futuro

router = APIRouter()

@router.post("/", response_model=schemas.user.User, status_code=status.HTTP_201_CREATED)
def create_user(
    *, 
    db: Session = Depends(get_db),
    user_in: schemas.user.UserCreate
    # current_user: models.User = Depends(get_current_active_superuser) # Proteger no futuro
) -> Any:
    """
    Cria um novo usuário. 
    TODO: Proteger este endpoint, e.g., apenas para superusuários ou primeiro usuário.
    """
    user = crud.user.get_user_by_email(db, email=user_in.email)
    if user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Um usuário com este email já existe no sistema.",
        )
    user = crud.user.create_user(db=db, obj_in=user_in)
    return user

@router.get("/", response_model=List[schemas.user.User])
def read_users(
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 100,
    # current_user: models.User = Depends(get_current_active_superuser) # Proteger no futuro
) -> Any:
    """Recupera uma lista de usuários."""
    users = crud.user.get_users(db, skip=skip, limit=limit)
    return users

# Adicionar mais endpoints de gerenciamento de usuário (get by id, update, delete) se necessário,
# lembrando de protegê-los adequadamente. 