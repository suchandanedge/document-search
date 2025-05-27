from ._anvil_designer import document_search_line_itemsTemplate
from anvil import *
import anvil.server

class document_search_line_items(document_search_line_itemsTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    row = self.item
    display_lines = []

    for key, value in row.items():
      display_lines.append(f'"{key}": "{value}"')

      self.db_items.text = "\n".join(display_lines)
