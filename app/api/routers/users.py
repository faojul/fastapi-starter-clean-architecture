from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from typing import List
from app.schemas.user import UserCreate, UserInDB, UserUpdate
from app.services.user_service import UserService
from app.repositories.user_repository import UserRepository
from app.api.dependencies import get_db, get_current_user
from app.models.user import User
from app.core.security import create_access_token, verify_password
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter(prefix="/users", tags=["user"])

@router.post("/token")
async def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: AsyncSession = Depends(get_db)
):
    user_repo = UserRepository(db)
    user = await user_repo.get_user_by_email(form_data.username)
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=400, detail="Incorrect email or password")
    access_token = create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}

@router.post("/", response_model=UserInDB)
async def create_user(user: UserCreate, db: AsyncSession = Depends(get_db)):
    user_service = UserService(UserRepository(db))
    return await user_service.create_user(user)

@router.get("/", response_model=List[UserInDB])
async def get_users(skip: int = 0, limit: int = 100, current_user: User = Depends(get_current_user), db: AsyncSession = Depends(get_db)):
    user_service = UserService(UserRepository(db))
    return await user_service.get_users(skip, limit, current_user)

@router.put("/{user_id}", response_model=UserInDB)
async def update_user(user_id: int, user_update: UserUpdate, current_user: User = Depends(get_current_user), db: AsyncSession = Depends(get_db)):
    user_service = UserService(UserRepository(db))
    return await user_service.update_user(user_id, user_update, current_user)

@router.delete("/{user_id}")
async def delete_user(user_id: int, current_user: User = Depends(get_current_user), db: AsyncSession = Depends(get_db)):
    user_service = UserService(UserRepository(db))
    await user_service.delete_user(user_id, current_user)
    return {"detail": "User deleted"}