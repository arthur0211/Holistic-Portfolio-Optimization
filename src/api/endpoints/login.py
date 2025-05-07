from datetime import timedelta
from typing import Any

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm # Formulário padrão para login
from sqlalchemy.orm import Session

from src.api import schemas # Importa o módulo de schemas
from src.core import crud, security
from src.core.config import settings
from src.db.session import get_db

router = APIRouter()

@router.post("/token", response_model=schemas.token.Token)
def login_for_access_token(
    db: Session = Depends(get_db), 
    form_data: OAuth2PasswordRequestForm = Depends()
) -> Any:
    """
    Endpoint para autenticação OAuth2 e obtenção de token de acesso.
    Utiliza o email como username.
    """
    user = crud.user.authenticate_user(
        db, email=form_data.username, password=form_data.password
    )
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Email ou senha incorretos",
            headers={"WWW-Authenticate": "Bearer"},
        )
    elif not crud.user.is_user_active(user):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail="Usuário inativo"
        )
    
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = security.create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

# Futuramente, podemos adicionar um endpoint para testar o token ou "me" endpoint
# from src.api.dependencies import get_current_user
# from src.core.models import User as DBUser # Evitar conflito com schema User
#
# @router.get("/me", response_model=schemas.user.User)
# def read_users_me(current_user: DBUser = Depends(get_current_user)):
#     """Retorna o usuário atual."""
#     return current_user 