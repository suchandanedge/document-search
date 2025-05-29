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
      raw_payload = record.get('m_payload', '{}')
      payload = json.loads(raw_payload)
      inward_lines = payload.get('inwardLines', [])
      for line in inward_lines:
        line_entry = {
          "item_name": line.get("item_name", ""),
          "units": line.get("units", ""),
          "lineNo": line.get("lineNo", ""),
          "product_code": line.get("product", {}).get("code", "")
        }
        flattened_records.append(line_entry)
    print(flattened_records)
    self.data_grid_1.columns = [
      {"id": "item_name", "title": "Item Name", "data_key": "item_name"},
      {"id": "units", "title": "Units", "data_key": "units"},
      {"id": "lineNo", "title": "Line No.", "data_key": "lineNo"},
      {"id": "product_code", "title": "Inward Ref", "data_key": "product_code"},
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
