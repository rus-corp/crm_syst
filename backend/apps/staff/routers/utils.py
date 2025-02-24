from core.models.utils import EmployeePosition


employee_position_variants = """Position Variants:\n
  Руководитель программы, Астроном, \n
  Астроном волонтер, Лектор, \n
  Фотограф, Фотограф волонтер,\n
  Повар, Волонтер на кухню"""



def positions_list():
  positions = [position.value for position in EmployeePosition]
  return {'positions': positions}