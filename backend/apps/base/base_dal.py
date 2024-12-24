from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import delete, select, insert, update


class BaseDAL:
  def __init__(self, db_session: AsyncSession):
    self.db_session = db_session
  
  
  async def base_create_item(self, model, values: dict, commit=False):
    """if commit = True -> session.commit() else session.flush()"""
    new_item = model(**values)
    self.db_session.add(new_item)
    if commit:
      await self.db_session.commit()
    else:
      await self.db_session.flush()
    return new_item
  
  
  async def base_get_all_items(self, model):
    query = select(model).order_by(model.id)
    result = await self.db_session.execute(query)
    return result.scalars().all()
  
  
  async def base_get_one_item(self, model, item_id: int):
    query = select(model).where(model.id == item_id)
    return await self.db_session.scalar(query)
  
  
  async def base_get_one_item_by_slug(self, model, item_slug: str):
    query = select(model).where(model.slug == item_slug)
    return await self.db_session.scalar(query)
  
  
  async def base_update_item(self, model, item_id: int, values):
    stmt = update(model).where(model.id == item_id).values(**values).returning(model)
    result = await self.db_session.execute(stmt)
    return result.scalar()
  
  
  async def base_delete_item(self, model, item_id: int) -> int:
    stmt = delete(model).where(model.id == item_id).returning(model.id)
    result = await self.db_session.execute(stmt)
    await self.db_session.commit()
    return result.scalar()
  
  
  async def base_get_or_create(self, model, values):
    query = select(model).filter_by(**values)
    instance = await self.db_session.scalar(query)
    if not instance:
      instance = await self.base_create_item(
        model=model,
        values=values
      )
    return instance