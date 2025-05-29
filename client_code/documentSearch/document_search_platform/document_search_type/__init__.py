from ._anvil_designer import document_search_typeTemplate
from anvil import *
import anvil.server
import json

class document_search_type(document_search_typeTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    db_data_records = self.item['records']
    self.label_doc_type.text = self.item['doc_id']
    # self.repeating_panel_records.items = db_data_records
    flattened_records = []
    for record in db_data_records:
      raw_payload = record.get('payload', '{}')
      payload = json.loads(raw_payload)
      payload['item_name'] = record.get('item_name', '')
      flattened_records.append(payload)
    print(flattened_records)
    self.data_grid_1.columns = [
      {"id": "item_name", "title": "Item Name", "data_key": "item_name"},
      {"id": "customer", "title": "Customer", "data_key": "customer"},
      {"id": "warehouse", "title": "Warehouse", "data_key": "warehouse"},
      {"id": "inwardReference", "title": "Inward Ref", "data_key": "inwardReference"},
      {"id": "inwardLines", "title": "Inward Lines", "data_key": "inwardLines"},
    ]
    self.repeating_panel_records.items = flattened_records
    self.date.text= self.item['records'][0]['log_date']

  def toggle_button_click(self, **event_args):
    if self.toggle_button.icon == 'fa:angle-right':
      self.toggle_button.icon = 'fa:angle-down'
      self.column_panel_1.visible = True
    else:
      self.toggle_button.icon = 'fa:angle-right'
      self.column_panel_1.visible = False
