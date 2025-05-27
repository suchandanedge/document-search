from ._anvil_designer import document_search_platformTemplate
from anvil import *
import anvil.server

class document_search_platform(document_search_platformTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.image_1.role = 'image-style'
    self.label_platform.text = self.item['platform_name']
    self.repeating_panel_types.items = self.item['types']
    # self.checkbox_status.checked = True
    if self.item['platform_name'] == "Mainfreight":
      self.image_1.source = "_/theme/mainfreight.png"
      self.image_1.background = 'white'
    else:
      self.image_1.source = "_/theme/netsuite.png"
      self.image_1.background = 'white'
    self.column_panel_2.role = 'vertical-line'
    # self.checkbox_status.role = 'status-complete'
    self.flow_panel_1.role = "scrollbar"
