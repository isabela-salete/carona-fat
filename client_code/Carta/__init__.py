from ._anvil_designer import CartaTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Carta(CartaTemplate):
  def __init__(self, ride, name, destiny, time, price, vagas, date, **properties):
    self.init_components(**properties)
    self.ride = ride
    self.nome.text = name
    self.destiny = destiny
    self.time = time
    self.price = price
    self.vagas = vagas
    self.date = date
    

    # Any code you write here will run before the form opens.
