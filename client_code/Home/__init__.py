from ._anvil_designer import HomeTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.users
from ..Caronas import Caronas
from ..Base import *


class Home(HomeTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)
   






