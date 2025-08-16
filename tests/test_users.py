import pytest
from fastapi.testclient import TestClient
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from app.main import app, async_session
from app.models.user import User, Role
from app.core.security import get_password_hash

@pytest.fixture
async def db_session():
    engine = create_async_engine("postgresql+asyncpg://user:password@localhost:5432/test_db")
    async with engine.begin() as conn:
        await conn.run_sync(User.metadata.create_all)
    Session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
    async with Session() as session:
        yield session
    async with engine.begin() as conn:
        await conn.run_sync(User.metadata.drop_all)
    await engine.dispose()

@pytest.fixture
def client(db_session):
    async def override_get_db():
        yield db_session
    app.dependency_overrides[async_session] = override_get_db
    return TestClient(app)

@pytest.fixture
async def test_user(db_session: AsyncSession):
    user = User(email="test@example.com", hashed_password=get_password_hash("password"), role=Role.USER)
    db_session.add(user)
    await db_session.commit()
    await db_session.refresh(user)
    return user

@pytest.fixture
async def admin_user(db_session: AsyncSession):
    user = User(email="admin@example.com", hashed_password=get_password_hash("password"), role=Role.ADMIN)
    db_session.add(user)
    await db_session.commit()
    await db_session.refresh(user)
    return user

@pytest.mark.asyncio
async def test_create_user(client: TestClient):
    response = client.post("/users", json={"email": "new@example.com", "password": "password", "role": "user"})
    assert response.status_code == 200
    assert response.json()["email"] == "new@example.com"

@pytest.mark.asyncio
async def test_login(client: TestClient, test_user):
    response = client.post("/token", data={"username": "test@example.com", "password": "password"})
    assert response.status_code == 200
    assert "access_token" in response.json()

@pytest.mark.asyncio
async def test_get_users_admin(client: TestClient, admin_user):
    response = client.post("/token", data={"username": "admin@example.com", "password": "password"})
    token = response.json()["access_token"]
    response = client.get("/users", headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 200
    assert isinstance(response.json(), list)

@pytest.mark.asyncio
async def test_get_users_non_admin(client: TestClient, test_user):
    response = client.post("/token", data={"username": "test@example.com", "password": "password"})
    token = response.json()["access_token"]
    response = client.get("/users", headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 403

@pytest.mark.asyncio
async def test_update_user_admin(client: TestClient, admin_user, test_user):
    response = client.post("/token", data={"username": "admin@example.com", "password": "password"})
    token = response.json()["access_token"]
    response = client.put(f"/users/{test_user.id}", json={"email": "updated@example.com"}, headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 200
    assert response.json()["email"] == "updated@example.com"

@pytest.mark.asyncio
async def test_delete_user_admin(client: TestClient, admin_user, test_user):
    response = client.post("/token", data={"username": "admin@example.com", "password": "password"})
    token = response.json()["access_token"]
    response = client.delete(f"/users/{test_user.id}", headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 200