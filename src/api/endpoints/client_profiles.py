import uuid
from typing import List, Any

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from src.api import schemas # Importa o módulo de schemas
from src.core import crud # Importa o módulo crud
from src.db.session import get_db

router = APIRouter()

@router.post("/", response_model=schemas.client_profile.ClientProfile, status_code=status.HTTP_201_CREATED)
def create_client_profile(
    *, 
    db: Session = Depends(get_db), 
    profile_in: schemas.client_profile.ClientProfileCreate
) -> Any:
    """Cria um novo perfil de cliente."""
    existing_profile_cpf = crud.client_profile.get_client_profile_by_cpf(db, cpf=profile_in.cpf)
    if existing_profile_cpf:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Um cliente com este CPF já existe no sistema.",
        )
    existing_profile_email = crud.client_profile.get_client_profile_by_email(db, email=profile_in.email)
    if existing_profile_email:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Um cliente com este email já existe no sistema.",
        )
    client_profile = crud.client_profile.create_client_profile(db=db, obj_in=profile_in)
    return client_profile

@router.get("/", response_model=List[schemas.client_profile.ClientProfile])
def read_client_profiles(
    db: Session = Depends(get_db), skip: int = 0, limit: int = 100
) -> Any:
    """Recupera uma lista de perfis de clientes."""
    client_profiles = crud.client_profile.get_client_profiles(db, skip=skip, limit=limit)
    return client_profiles

@router.get("/{client_id}", response_model=schemas.client_profile.ClientProfile)
def read_client_profile(
    *, db: Session = Depends(get_db), client_id: uuid.UUID
) -> Any:
    """Recupera um perfil de cliente pelo ID."""
    client_profile = crud.client_profile.get_client_profile(db, client_id=client_id)
    if not client_profile:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Perfil de cliente não encontrado")
    return client_profile

@router.put("/{client_id}", response_model=schemas.client_profile.ClientProfile)
def update_client_profile(
    *,
    db: Session = Depends(get_db),
    client_id: uuid.UUID,
    profile_in: schemas.client_profile.ClientProfileUpdate,
) -> Any:
    """Atualiza um perfil de cliente."""
    client_profile = crud.client_profile.get_client_profile(db, client_id=client_id)
    if not client_profile:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Perfil de cliente não encontrado")
    
    # Verifica se o CPF está sendo atualizado para um já existente (e diferente do atual)
    if profile_in.cpf and profile_in.cpf != client_profile.cpf:
        existing_profile_cpf = crud.client_profile.get_client_profile_by_cpf(db, cpf=profile_in.cpf)
        if existing_profile_cpf:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Um cliente com este CPF já existe no sistema.",
            )
            
    # Verifica se o email está sendo atualizado para um já existente (e diferente do atual)
    if profile_in.email and profile_in.email != client_profile.email:
        existing_profile_email = crud.client_profile.get_client_profile_by_email(db, email=profile_in.email)
        if existing_profile_email:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Um cliente com este email já existe no sistema.",
            )

    client_profile = crud.client_profile.update_client_profile(db=db, db_obj=client_profile, obj_in=profile_in)
    return client_profile

@router.delete("/{client_id}", response_model=schemas.client_profile.ClientProfile)
def delete_client_profile(
    *, db: Session = Depends(get_db), client_id: uuid.UUID
) -> Any:
    """Deleta um perfil de cliente."""
    client_profile = crud.client_profile.get_client_profile(db, client_id=client_id)
    if not client_profile:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Perfil de cliente não encontrado")
    client_profile = crud.client_profile.remove_client_profile(db=db, client_id=client_id)
    return client_profile 