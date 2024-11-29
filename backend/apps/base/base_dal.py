from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import delete, select


class BaseDAL:
  def __init__(self, db_session: AsyncSession):
    self.db_session = db_session
  
  
  async def base_get_all_items(self, model):
    query = select(model).order_by(model.id)
    result = await self.db_session.execute(query)
    return result.scalars().all()
  
  
  async def base_get_one_item(self, model, item_id):
    query = select(model).where(model.id == item_id)
    return await self.db_session.scalar(query)
  
  
  async def base_delete_item(self, model, item_id: int):
    stmt = delete(model).where(model.id == item_id).returning(model.id)
    result = await self.db_session.execute(stmt)
    await self.db_session.commit()
    return result.scalar()