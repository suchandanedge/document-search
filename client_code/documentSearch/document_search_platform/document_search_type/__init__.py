from ._anvil_designer import document_search_typeTemplate
from anvil import *
import anvil.server

class document_search_type(document_search_typeTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    db_data_records = self.item['records']
    self.label_doc_type.text = self.item['doc_id']
    # self.repeating_panel_records.items = db_data_records
    self.repeating_panel_1.items = db_data_records
    print(self.item)
    self.date.text= self.item['records'][0]['log_date']

  def toggle_button_click(self, **event_args):
    if self.toggle_button.icon == 'fa:angle-right':
      self.toggle_button.icon = 'fa:angle-down'
      self.column_panel_1.visible = True
    else:
      self.toggle_button.icon = 'fa:angle-right'
      self.column_panel_1.visible = False
