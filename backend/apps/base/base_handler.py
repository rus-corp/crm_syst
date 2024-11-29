from sqlalchemy.ext.asyncio import AsyncSession




class BaseHandler:
  def __init__(self, session: AsyncSession):
    self.session = session