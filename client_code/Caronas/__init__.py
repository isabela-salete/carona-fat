from ._anvil_designer import CaronasTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..Criar_carona import Criar_carona
import anvil.users

class Caronas(CaronasTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)

  def criar_carona_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.column_panel_1.clear()
    self.column_panel_1.add_component(Criar_carona())
    pass

