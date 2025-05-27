from ._anvil_designer import document_search_typeTemplate
from anvil import *
import anvil.server

class document_search_type(document_search_typeTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.label_doc_type.text = self.item['doc_type_name']
    self.repeating_panel_records.items = self.item['records']
