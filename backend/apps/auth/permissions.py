


from core.models.user_models import User
from core.models.utils import UserRole


class Permissions:
  def __init__(self, current_user: User=None) -> None:
    self.current_user = current_user


  def superuser_permission(self):
    if self.current_user.role == UserRole.SP:
      return True
    return False
  
  
  def admin_permission(self):
    if self.current_user.role == UserRole.AD:
      return True
    return False

  def manager_permission(self):
    if self.current_user.role == UserRole.MG:
      return True
    return False


  def spritzer_permission(self):
    if self.current_user.role == UserRole.SP:
      return True
    return False