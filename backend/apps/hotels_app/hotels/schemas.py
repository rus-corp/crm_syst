from typing import List, Optional
from pydantic import BaseModel, ConfigDict

from ..hotel_rooms.schemas import RoomForHotelResponse, RoomForAppendToProgramResponse
from apps.program_app.schemas import ProgramResponseForAppendHoteAndRoom


class HotelBase(BaseModel):
  title: str
  address: str
  contacts: str
  city: str
  email: str
  
  model_config = ConfigDict(from_attributes=True)



class CreateHotelRequest(HotelBase):
  desc: Optional[str] = None



class HotelBaseResponse(CreateHotelRequest):
  id: int



class HotelUpdateRequest(BaseModel):
  model_config = ConfigDict(from_attributes=True)
  
  title: Optional[str] = None
  address: Optional[str] = None
  contacts: Optional[str] = None
  city: Optional[str] = None
  email: Optional[str] = None
  desc: Optional[str] = None



class HotelWithRooms(HotelBaseResponse):
  rooms: Optional[List[RoomForHotelResponse]] = []
  hotel_rooms_volume: Optional[int] = None




class AppendHotelAndRoomToProgram(BaseModel):
  program_id: int
  hotel_id: int
  room_id: int


class HotelForAppendToProgramResponse(BaseModel):
  id: int
  title: str
  city: str
  contacts: str



class ProgramHotelRoomResponse(BaseModel):
  program: ProgramResponseForAppendHoteAndRoom
  hotel: HotelForAppendToProgramResponse
  room: RoomForAppendToProgramResponse



