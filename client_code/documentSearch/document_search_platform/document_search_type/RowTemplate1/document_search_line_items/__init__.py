from ._anvil_designer import document_search_line_itemsTemplate
from anvil import *
import anvil.server

class document_search_line_items(document_search_line_itemsTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
