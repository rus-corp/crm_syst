from fastapi.exceptions import HTTPException
from fastapi import status



class AppBaseExceptions:
  @staticmethod
  def relation_not_exsist(main_model: str, main_item_id: int, second_model: str, second_item_id: int):
    raise HTTPException(
      status_code=status.HTTP_404_NOT_FOUND,
      detail=f'Relation between {main_model} with id {main_item_id} and {second_model} with {second_item_id} does not found'
    )
  
  
  @staticmethod
  def item_not_found(item_data: str):
    raise HTTPException(
      status_code=status.HTTP_404_NOT_FOUND,
      detail=f'{item_data} not found'
    )
  
  @staticmethod
  def item_create_error(item_data: str):
    raise HTTPException(
      status_code=status.HTTP_403_FORBIDDEN,
      detail=f'Does not create {item_data}'
    )
  
  
  @staticmethod
  def need_data(item_data: str):
    raise HTTPException(
      status_code=status.HTTP_404_NOT_FOUND,
      detail=f'Need Data {item_data} for create'
    )