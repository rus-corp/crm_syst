from typing import List
from core.models.association_models import ProgramClientRoom


def check_sharing(program_room_clients: List[ProgramClientRoom]) -> bool:
  if not program_room_clients:
    return False
  for program_room in program_room_clients:
    return program_room.no_sharing



def check_free_room_volume(program_room_clients: List[ProgramClientRoom]) -> int:
  room_current_client = len(program_room_clients)
  for program_room in program_room_clients:
    room_volume = program_room.program_room.room.room_volume
    return room_volume - room_current_client