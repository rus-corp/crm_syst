from typing import Optional
from pydantic import BaseModel, ConfigDict



class HoteRoomBase(BaseModel):
  model_config = ConfigDict(from_attributes=True)
  
  room_type: str
  room_price: int
  room_volume: int
  hotel_id: int


class HoteRoomCreateRequset(HoteRoomBase):
  pass


class HotelRoomUpdateRequest(BaseModel):
  model_config = ConfigDict(from_attributes=True)
  room_type: Optional[str] = None
  room_price: Optional[int] = None
  room_volume: Optional[int] = None
  hotel_id: Optional[int] = None



class RoomForHotelResponse(BaseModel):
  model_config = ConfigDict(from_attributes=True)
  
  room_type: str
  room_price: int
  room_volume: int



class RoomForAppendToProgramResponse(BaseModel):
  id: int
  room_type: str
  room_volume: int
  room_price: int