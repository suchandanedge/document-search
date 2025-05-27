from ._anvil_designer import document_search_typeTemplate
from anvil import *
import anvil.server

class document_search_type(document_search_typeTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    db_data_records = self.item['records']
    self.label_doc_type.text = self.item['doc_type_name']
    self.repeating_panel_records.items = db_data_records
    item_count = len(self.item['records'])
    self.item_count.text = item_count
    total_ship_qty = sum(
      int(row.get("ship_qty", 0)) if str(row.get("ship_qty", "")).isdigit() else 0
      for row in db_data_records
    )
    self.total_ship_qty.text = total_ship_qty

  def toggle_button_click(self, **event_args):
    if self.toggle_button.icon == 'fa:angle-right':
      self.toggle_button.icon = 'fa:angle-down'
      self.column_panel_1.visible = True
    else:
      self.toggle_button.icon = 'fa:angle-right'
      self.column_panel_1.visible = False
