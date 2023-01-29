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
    self.init_components(**properties)

    

  def enviar_click(self, **event_args):
    ride = self.ride.selected_value 
    name = self.name.text
    destiny = self.destiny.text
    time = self.time.text
    price = self.price.text
    vagas = self.vagas.text
    date =self.date.date
    try:
     anvil.server.call('add_text', ride, name, destiny, time, price, vagas, date)
     Notification("A carona foi enviada com sucesso").show()
    except Exception as e:
      Notification(e).show()





 






  
