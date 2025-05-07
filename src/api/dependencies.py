from typing import Optional, Any
import uuid

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from pydantic import ValidationError
from sqlalchemy.orm import Session

from src.core import crud, models, security # security para decode_access_token
from src.api.schemas import token as token_schema # Renomeado para evitar conflito
from src.core.config import settings
from src.db.session import get_db

reusable_oauth2 = OAuth2PasswordBearer(
    tokenUrl=f"{settings.API_V1_STR}/login/token" 
)

def get_current_user(
    db: Session = Depends(get_db),
    token: str = Depends(reusable_oauth2)
) -> models.User:
    """
    Dependência para obter o usuário atual a partir do token JWT.
    Levanta HTTPException 401 se o token for inválido ou o usuário não for encontrado/ativo.
    """
    try:
        payload = security.decode_access_token(token)
        if payload is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Não foi possível validar as credenciais (payload nulo)",
                headers={"WWW-Authenticate": "Bearer"},
            )
        token_data = token_schema.TokenPayload(**payload) 
    except (JWTError, ValidationError) as e:
        # Log do erro pode ser útil aqui: print(f"Erro de token: {e}")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Não foi possível validar as credenciais (erro de decodificação/validação)",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    if token_data.sub is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Não foi possível validar as credenciais (sub faltante)",
            headers={"WWW-Authenticate": "Bearer"},
        )

    # No nosso caso, o 'sub' será o email do usuário ou o ID do usuário.
    # Se for ID, precisaremos converter para UUID se for o caso.
    # Por simplicidade, vamos assumir que 'sub' é o email por enquanto.
    # user = crud.user.get_user(db, user_id=token_data.sub) # Se sub fosse user_id (UUID)
    user = crud.user.get_user_by_email(db, email=token_data.sub)

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuário não encontrado")
    if not crud.user.is_user_active(user):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Usuário inativo")
    return user

# Opcional: Dependência para superusuário
# def get_current_active_superuser(
#     current_user: models.User = Depends(get_current_user),
# ) -> models.User:
#     if not crud.user.is_superuser(current_user):
#         raise HTTPException(
#             status_code=400, detail="O usuário não tem privilégios suficientes"
#         )
#     return current_user 