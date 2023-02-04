from ._anvil_designer import CaronasTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..Criar_carona import Criar_carona
from ..Carta import Carta
from ..Bus import Bus
import anvil.users

class Caronas(CaronasTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)
    self.carregar_caronas()
    
  def criar_carona_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.column_panel_1.clear()
    self.column_panel_1.add_component(Criar_carona())
    pass

  def carregar_caronas(self):
    caronas = anvil.server.call("get_carona").search(tables.order_by("date", ascending=False))
    caronas_panel = GridPanel()

    for i, carona in enumerate(caronas):
     c = Carta(name=carona['name'], ride=carona['ride'],destiny=carona['destiny'], time=carona['time'], price=carona['price'], vagas=carona['vagas'], date=carona['date'])
     caronas_panel.add_component(c, row=str(i//2), width_xs=6)
     
    self.column_panel_1.add_component(caronas_panel)

  def onibus_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.column_panel_1.clear()
    self.column_panel_1.add_component(Bus())
    pass

