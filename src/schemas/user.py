from pydantic import BaseModel,EmailStr, Field

class UserCreate(BaseModel):
    email: EmailStr
    password: str
    is_active: bool = False
    is_superuser: bool = False