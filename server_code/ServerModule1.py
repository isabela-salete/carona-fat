import anvil.google.auth, anvil.google.drive, anvil.google.mail
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

@anvil.server.callable
def add_text(ride, name, destiny, time, price, vagas, date):   #receber a informação e colocar na tabela
  app_tables.carona.add_row(ride=ride, name=name, destiny=destiny, time=time, price=price, vagas=vagas, date=date)

@anvil.server.callable
def add_vaga(vaga1, vaga2, vaga3, vaga4):   #receber a informação e colocar na tabela
  app_tables.vagas.add_row(vaga1=vaga1, vaga2=vaga2, vaga3=vaga3, vaga4=vaga4)  

@anvil.server.callable
def get_carona():
    return app_tables.carona.client_writable(tables.order_by("date", ascending=True))

@anvil.server.callable
def get_vagas():
    return app_tables.vagas.client_writable(tables.order_by("date", ascending=True))
  



  

  
