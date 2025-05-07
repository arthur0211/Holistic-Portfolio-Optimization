import uuid
from typing import Any, Dict, Optional, Union, List

from sqlalchemy.orm import Session

from src.core.models import ClientProfile
from src.api.schemas.client_profile import ClientProfileCreate, ClientProfileUpdate

# Funções CRUD para o modelo ClientProfile

def get_client_profile(db: Session, client_id: uuid.UUID) -> Optional[ClientProfile]:
    """Busca um perfil de cliente pelo ID."""
    return db.query(ClientProfile).filter(ClientProfile.id == client_id).first()

def get_client_profile_by_cpf(db: Session, cpf: str) -> Optional[ClientProfile]:
    """Busca um perfil de cliente pelo CPF."""
    return db.query(ClientProfile).filter(ClientProfile.cpf == cpf).first()

def get_client_profile_by_email(db: Session, email: str) -> Optional[ClientProfile]:
    """Busca um perfil de cliente pelo email."""
    return db.query(ClientProfile).filter(ClientProfile.email == email).first()

def get_client_profiles(
    db: Session, skip: int = 0, limit: int = 100
) -> List[ClientProfile]:
    """Busca uma lista de perfis de cliente com paginação."""
    return db.query(ClientProfile).offset(skip).limit(limit).all()

def create_client_profile(db: Session, *, obj_in: ClientProfileCreate) -> ClientProfile:
    """Cria um novo perfil de cliente."""
    db_obj = ClientProfile(
        full_name=obj_in.full_name,
        cpf=obj_in.cpf,
        email=obj_in.email,
        # Adicionar outros campos de ClientProfileCreate conforme necessário
        phone_number=obj_in.phone_number,
        date_of_birth=obj_in.date_of_birth,
        risk_number=obj_in.risk_number,
        risa_quadrant=obj_in.risa_quadrant,
        behavioral_biases_scores=str(obj_in.behavioral_biases_scores) if obj_in.behavioral_biases_scores else None, # Salva como string JSON
        investment_objectives=obj_in.investment_objectives,
        financial_situation=obj_in.financial_situation,
        product_knowledge=obj_in.product_knowledge,
    )
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def update_client_profile(
    db: Session, *, db_obj: ClientProfile, obj_in: Union[ClientProfileUpdate, Dict[str, Any]]
) -> ClientProfile:
    """Atualiza um perfil de cliente existente."""
    if isinstance(obj_in, dict):
        update_data = obj_in
    else:
        update_data = obj_in.model_dump(exclude_unset=True) # Usar model_dump

    if "behavioral_biases_scores" in update_data and update_data["behavioral_biases_scores"] is not None:
        update_data["behavioral_biases_scores"] = str(update_data["behavioral_biases_scores"])

    for field in update_data:
        if hasattr(db_obj, field):
            setattr(db_obj, field, update_data[field])
    
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def remove_client_profile(db: Session, *, client_id: uuid.UUID) -> Optional[ClientProfile]:
    """Remove um perfil de cliente pelo ID."""
    obj = db.query(ClientProfile).get(client_id)
    if obj:
        db.delete(obj)
        db.commit()
    return obj 