from sqlalchemy.orm import Session

from schemas.user import UserCreate
from models.user import User
from utils.hasher import Hasher

def create_new_user(obj: UserCreate, db: Session):
    user = User(
        email=obj.email,
        password=Hasher.get_password_hash(obj.password),
        is_active=obj.is_active,
        is_superuser=obj.is_superuser
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
