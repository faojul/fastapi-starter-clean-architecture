from fastapi import FastAPI
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from app.core.config import settings
from app.api.routers import users
from app.models.user import Base

app = FastAPI(
    title="My Awesome API",
    description="This is my FastAPI project with Swagger docs",
    version="1.0.0",
    contact={
        "name": "Your Name",
        "email": "your-email@example.com"
    },
    docs_url="/swagger",  # change Swagger UI URL if you want
    redoc_url="/redoc",   # change Redoc URL if you want
)

async_engine = create_async_engine(settings.DATABASE_URL, echo=True)
async_session = sessionmaker(async_engine, class_=AsyncSession, expire_on_commit=False)

@app.on_event("startup")
async def startup_event():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

app.include_router(users.router)