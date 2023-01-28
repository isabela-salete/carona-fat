import anvil.google.auth, anvil.google.drive, anvil.google.mail
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

@anvil.server.callable
def add_text(ride, name, destiny, time, price, vagas):   #receber a informação e colocar na tabela
  app_tables.carona.add_row(ride=ride, name=name, destiny=destiny, time=time, price=price, vagas=vagas)

@anvil.server.callable
def get_carona():
  return app_tables.carona.client_readable()

  
