from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column



class Base(DeclarativeBase):
  __abstract__ = True
  
  id: Mapped[int] = mapped_column(primary_key=True)




from config import DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME

DATABASE_URL = f'postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'

engine = create_async_engine(DATABASE_URL, echo=True)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)






async def get_db():
  try:
    session: AsyncSession = async_session_maker()
    yield session
  finally:
      await session.close()