from sqlalchemy.ext.asyncio import AsyncSession
from apps.base.base_handler import BaseHandler
from .. import schemas
from apps.utils.slug import create_slug
from ..utils import program_response_format
from apps.base.exceptions import AppBaseExceptions
from ..dals.program_dal import ProgramDAL


class ProgramBaseHandler(BaseHandler):
  def __init__(self, session: AsyncSession):
    self.session = session
    self.program_dal = ProgramDAL(self.session)
  
  
  async def _create_program(
    self,
    create_program_body: schemas.CreateProgramRequets
  ) -> schemas.ProgramBaseResponse:
    async with self.session.begin():
      body_data = create_program_body.model_dump(exclude_none=True)
      slug = create_slug(body_data['title'] + str(body_data['start_date']))
      body_data['slug'] = slug
      created_program = await self.program_dal.create_program(**body_data)
      return program_response_format(created_program)
  
  
  async def _get_programs_list(self):
    programs_list = await self.program_dal.get_active_programs()
    programs = []
    for program in programs_list: # type Program
      programs.append(program_response_format(program, duration=True))
    return programs
  
  
  async def _get_program_by_slug(
    self,
    program_slug: str
  ):
    program = await self.program_dal.get_program_by_slug(program_slug)
    return program_response_format(program, duration=True)
  
  
  async def _update_program(
    self,
    program_slug: str,
    values: schemas.ProgramUpdateRequest
  ):
    async with self.session.begin():
      body_data = values.model_dump(exclude_none=True)
      updated_program = await self.program_dal.update_program_by_slug(
        program_slug=program_slug,
        values=body_data
      )
      if updated_program is None:
        return AppBaseExceptions.item_not_found('Program')
      return program_response_format(updated_program, duration=True)
  
  
  async def _get_program_prices(self, program_id: int):
    program_prices = await self.program_dal.get_program_prices(program_id)
    # program_price_res = schemas.ProgramPricesBaseResponse(
    #   id=program_prices.prices.id,
    # )
    return schemas.ProgramPricesResponse(
      id=program_prices.id,
      title=program_prices.title,
      start_date=program_prices.start_date,
      end_date=program_prices.end_date,
      place=program_prices.place,
      desc=program_prices.desc,
      slug=program_prices.slug,
      status=program_prices.status,
      client_count=program_prices.client_count,
      duration=program_prices.duration(),
      prices=program_prices.prices,
    )