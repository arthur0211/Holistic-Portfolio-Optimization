from typing import Optional
import uuid # Import uuid for user_id if it's a UUID

from pydantic import BaseModel

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenPayload(BaseModel):
    sub: Optional[str] = None # 'sub' is standard for subject (e.g., user identifier)
    # Você pode adicionar outros campos ao payload se necessário, como:
    # user_id: Optional[uuid.UUID] = None
    # roles: Optional[list[str]] = None 