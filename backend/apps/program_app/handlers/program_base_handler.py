from apps.base.base_handler import BaseHandler
from .. import schemas
from apps.utils.slug import create_slug
from ..utils import program_response_format
from apps.base.exceptions import AppBaseExceptions



class ProgramBaseHandler(BaseHandler):

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