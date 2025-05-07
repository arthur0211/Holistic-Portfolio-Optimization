import uuid
from datetime import date, datetime
from typing import Optional, Dict, Any

from pydantic import BaseModel, EmailStr, constr, validator

from src.core.models import RISAQuadrant # Importando o Enum do SQLAlchemy model

# Schema base com campos comuns a todas as variações
class ClientProfileBase(BaseModel):
    full_name: Optional[str] = None
    email: Optional[EmailStr] = None
    phone_number: Optional[str] = None
    date_of_birth: Optional[date] = None
    risk_number: Optional[int] = None
    risa_quadrant: Optional[RISAQuadrant] = None
    behavioral_biases_scores: Optional[Dict[str, Any]] = None # Aceita um dicionário JSON
    investment_objectives: Optional[str] = None
    financial_situation: Optional[str] = None
    product_knowledge: Optional[str] = None

    @validator('cpf', pre=True, always=True, check_fields=False)
    def validate_cpf_format(cls, v):
        if v is not None and not v.isdigit():
            raise ValueError("CPF deve conter apenas dígitos")
        return v

# Schema para criação de um perfil de cliente (campos obrigatórios aqui)
class ClientProfileCreate(ClientProfileBase):
    full_name: str
    cpf: constr(min_length=11, max_length=11) # CPF com 11 dígitos
    email: EmailStr

# Schema para atualização de um perfil de cliente (todos os campos são opcionais)
class ClientProfileUpdate(ClientProfileBase):
    cpf: Optional[constr(min_length=11, max_length=11)] = None

# Propriedades compartilhadas por modelos armazenados no DB
class ClientProfileInDBBase(ClientProfileBase):
    id: uuid.UUID
    created_at: datetime
    updated_at: datetime
    cpf: str # CPF é obrigatório e imutável após a criação, mas presente no DB

    class Config:
        from_attributes = True # Anteriormente orm_mode = True

# Schema para retornar um perfil de cliente da API (o que é exposto)
class ClientProfile(ClientProfileInDBBase):
    pass

# Poderíamos ter um schema para listar múltiplos perfis também, se necessário
# class ClientProfileList(BaseModel):
#     items: list[ClientProfile]
#     total: int 