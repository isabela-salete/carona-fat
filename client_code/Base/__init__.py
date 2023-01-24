from ._anvil_designer import BaseTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.users
from ..Home import *

class Base(BaseTemplate):
  def __init__(self, **properties):
    self.change_sign_user()
    self.init_components(**properties)
    self.content_panel.add_component(Home())
    
  def change_sign_user(self):
    user = anvil.users.get_user()
    if user:
      email = user["email"]
      self.user_te.text = email

    else:
      self.user_te.text = "Usuário"
 

    # Any code you write here will run before the form opens.

  def label_3_show(self, **event_args):
    """This method is called when the Label is shown on the screen"""
    pass

  def login_click(self, **event_args):
    user = anvil.users.get_user()
    if user:
      logout = confirm(f"{user['email']}, voce realmente quer sair?")
      if logout:
        anvil.users.logout()    
    else:
      anvil.users.login_with_form(allow_cancel=True)
    self.change_sign_user()
  


