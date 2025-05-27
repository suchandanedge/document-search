from ._anvil_designer import document_search_platformTemplate
from anvil import *
import anvil.server

class document_search_platform(document_search_platformTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.label_platform.text = self.item['platform_name']
    self.repeating_panel_types.items = self.item['types']
    self.checkbox_status.checked = True
    self.column_panel_2.role = 'vertical-line'
    self.checkbox_status.role = 'status-complete'
    self.flow_panel_1.role = "scrollbar"
