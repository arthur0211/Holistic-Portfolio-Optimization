import uuid
from typing import Optional
from datetime import datetime

from pydantic import BaseModel, EmailStr

# Propriedades compartilhadas básicas do usuário
class UserBase(BaseModel):
    email: Optional[EmailStr] = None
    is_active: Optional[bool] = True
    # is_superuser: bool = False # Se tivermos superusuários
    full_name: Optional[str] = None

# Propriedades para receber na criação do usuário
class UserCreate(UserBase):
    email: EmailStr
    password: str # Senha em texto plano, será hashada no CRUD
    full_name: Optional[str] = None

# Propriedades para receber na atualização do usuário
class UserUpdate(UserBase):
    password: Optional[str] = None # Senha em texto plano, será hashada no CRUD

# Propriedades compartilhadas por modelos armazenados no DB
class UserInDBBase(UserBase):
    id: uuid.UUID
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True # Anteriormente orm_mode = True

# Propriedades adicionais para retornar via API (o que é exposto)
class User(UserInDBBase):
    pass

# Propriedades adicionais armazenadas no DB (não necessariamente expostas)
class UserInDB(UserInDBBase):
    hashed_password: str 