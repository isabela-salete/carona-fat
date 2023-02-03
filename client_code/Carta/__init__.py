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
  def __init__(self, ride, name, destiny, time, price, vagas, **properties):
    self.init_components(**properties)
    self.tipo.text = ride
    self.nome.text = name
    self.destino.text = destiny
    self.saida.text = time
    self.dinheiro.text = price
    self.vagaa.text = vagas
    #self.date.date = date
    

    # Any code you write here will run before the form opens.
