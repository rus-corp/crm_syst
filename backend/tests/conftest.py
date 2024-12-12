import asyncio
from typing import AsyncGenerator, Any
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase, sessionmaker
from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession, create_async_engine
import pytest
from httpx import AsyncClient
from fastapi.testclient import TestClient
from sqlalchemy.pool import NullPool


from core.database import get_db, Base
from config import DB_NAME_TEST, DB_PORT_TEST, DB_USER, DB_PASSWORD, DB_HOST_TEST
from main import app


DATABASE_URL_TEST = f'postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST_TEST}:{DB_PORT_TEST}/{DB_NAME_TEST}'
engine_test = create_async_engine(DATABASE_URL_TEST, future=True, poolclass=NullPool)
async_session_maker = async_sessionmaker(engine_test, class_=AsyncSession, expire_on_commit=False)
Base.metadata.bind=engine_test


async def override_get_async_session() -> AsyncGenerator[AsyncSession, None]:
  async with async_session_maker() as session:
    yield session


app.dependency_overrides[get_db] = override_get_async_session

@pytest.fixture(scope='session', autouse=True)
async def prepare_db():
  async with engine_test.begin() as conn:
    await conn.run_sync(Base.metadata.create_all)
  yield
  
  async with engine_test.begin() as conn:
    await conn.run_sync(Base.metadata.drop_all)


@pytest.fixture(scope='session')
def get_event_loop():
  loop = asyncio.get_event_loop_policy().new_event_loop()
  yield loop
  loop.close()


@pytest.fixture
async def ac() -> AsyncGenerator[AsyncClient, None]:
  async with AsyncClient(app=app, base_url='http://test') as ac:
    yield ac
