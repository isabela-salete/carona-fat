from ._anvil_designer import Criar_caronaTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Criar_carona(Criar_caronaTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def enviar_click(self, **event_args):
    ride = self.ride.selected_value 
    name = self.name.text
    destiny = self.destiny.text
    time = self.time.text
    try:
     anvil.server.call('add_txt', name, destiny, time)
     Notification("A mensagem foi enviada com sucesso").show()
    except Exception as e:
      Notification(e).show()





  
