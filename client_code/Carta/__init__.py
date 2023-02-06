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
    #vaga1 = self.v1.text
    #vaga2 = self.v2.text
    #vaga3 = self.v3.text
    #vaga4 = self.v4.text
    if user:  
      email = user["email"]
      self.v1.text = email
      #anvil.server.call('add_vaga', vaga1, vaga2, vaga3, vaga4)
    else: 
     pass

  def pegar_v2_click(self, **event_args):
    """This method is called when the button is clicked"""
    user = anvil.users.get_user()
    if user:
      email = user["email"]
      self.v2.text = email
    else: 
     pass

  def pegar_v3_click(self, **event_args):
    """This method is called when the button is clicked"""
    user = anvil.users.get_user()
    if user:
      email = user["email"]
      self.v3.text = email
    else: 
     pass

  def pegar_v4_click(self, **event_args):
    """This method is called when the button is clicked"""
    user = anvil.users.get_user()
    if user:
      email = user["email"]
      self.v4.text = email
    else: 
     pass



      




