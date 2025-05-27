from ._anvil_designer import documentSearchTemplate
from anvil import *
import anvil.server

class documentSearch(documentSearchTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

  def button_1_click(self, **event_args):
    self.flow_panel_3.visible = True
    self.column_panel_1.visible=True
    self.flow_panel_5.visible=True
    search_text = self.search_box.text.strip()
    if not search_text:
      return

    result = anvil.server.call('document_search', search_text)
    if isinstance(result, dict) and "error" in result:
      alert(result["error"])
      return
    grouped_data = {}
    for row in result:
      platform = row.get("platform", "Unknown")
      doc_type = row.get("type", "Unknown")

      if platform not in grouped_data:
        grouped_data[platform] = {}

      if doc_type not in grouped_data[platform]:
        grouped_data[platform][doc_type] = []

      grouped_data[platform][doc_type].append(row)
    platform_rows = []
    for platform, types_dict in grouped_data.items():
      type_rows = []
      for doc_type, records in types_dict.items():
        type_rows.append({
          "doc_type_name": doc_type,
          "records": records
        })
      platform_rows.append({
        "platform_name": platform,
        "types": type_rows
      })
    self.repeating_panel_platforms.items = platform_rows

  def search_box_pressed_enter(self, **event_args):
    self.flow_panel_3.visible = True
    self.column_panel_1.visible=True
    self.flow_panel_5.visible=True

