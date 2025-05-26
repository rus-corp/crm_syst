from sqlalchemy.ext.asyncio import AsyncSession

from core.models.user_models import User
from apps.auth.permissions import Permissions



class BaseHandler:
  def __init__(self, session: AsyncSession, current_user: User=None):
    self.session = session
    self.current_user = current_user
    self.permissions = Permissions(current_user)