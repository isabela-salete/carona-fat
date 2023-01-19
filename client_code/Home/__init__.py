from ._anvil_designer import HomeTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.users
from ..Caronas import Caronas

class Home(HomeTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def botao_carona_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.column_panel.clear()
    self.column_panel.add_component(Caronas())
    pass

  def login_click(self, **event_args):
    anvil.users.login_with_form()
    pass





