from pydantic import BaseModel
from pathlib import Path
from config import settings


class AuthJWT(BaseModel):
  private_key_path: Path = settings.BASE_DIR / "certs" / "jwt-private.pem"
  public_key_path: Path = settings.BASE_DIR / "certs" / "jwt-public.pem"
  access_token_expire_minutes: int = 60
  algorithm: str = settings.ALGORITHM