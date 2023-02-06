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
  def __init__(self, ride, name, destiny, time, price, date, vagas, **properties):
    self.init_components(**properties)
    self.tipo.text = ride
    self.nome.text = name
    self.destino.text = destiny
    self.saida.text = time
    self.dinheiro.text = price
    self.vagaa.text = vagas
    self.dia.date = date


    # Any code you write here will run before the form opens.

  def pegar_click(self, **event_args):
    """This method is called when the button is clicked"""
    user = anvil.users.get_user()
    if user:
      email = user["email"]
      self.v1.text = email
    pass




