from app.repositories.user_repository import UserRepository
from app.schemas.user import UserCreate, UserUpdate
from app.models.user import User, Role
from fastapi import HTTPException, status

class UserService:
    def __init__(self, user_repo: UserRepository):
        self.user_repo = user_repo

    async def create_user(self, user: UserCreate) -> User:
        existing_user = await self.user_repo.get_user_by_email(user.email)
        if existing_user:
            raise HTTPException(status_code=400, detail="Email already registered")
        return await self.user_repo.create_user(user)

    async def get_users(self, skip: int = 0, limit: int = 100, current_user: User = None) -> list[User]:
        if current_user.role not in [Role.ADMIN, Role.MANAGEMENT]:
            raise HTTPException(status_code=403, detail="Not authorized")
        return await self.user_repo.get_users(skip, limit)

    async def update_user(self, user_id: int, user_update: UserUpdate, current_user: User) -> User:
        if current_user.role != Role.ADMIN:
            raise HTTPException(status_code=403, detail="Only admins can update users")
        updated_user = await self.user_repo.update_user(user_id, user_update)
        if not updated_user:
            raise HTTPException(status_code=404, detail="User not found")
        return updated_user

    async def delete_user(self, user_id: int, current_user: User) -> bool:
        if current_user.role != Role.ADMIN:
            raise HTTPException(status_code=403, detail="Only admins can delete users")
        success = await self.user_repo.delete_user(user_id)
        if not success:
            raise HTTPException(status_code=404, detail="User not found")
        return success