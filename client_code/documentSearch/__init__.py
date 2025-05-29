from ._anvil_designer import documentSearchTemplate
from anvil import *
import anvil.server

class documentSearch(documentSearchTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.column_panel_1.role = "search-result-card"
    self.flow_panel_2.role = "search-card"
  def button_1_click(self, **event_args):
    self.run_search(self.search_box.text.strip())


  def search_box_pressed_enter(self, **event_args):
    self.run_search(self.search_box.text.strip())

  def run_search(self, search_text):
    self.flow_panel_3.visible = True
    self.column_panel_1.visible=True
    self.flow_panel_5.visible=True
    if not search_text:
      return

    result = anvil.server.call('document_search', search_text)
    if isinstance(result, dict) and "error" in result:
      alert(result["error"])
      return

    grouped_data = {}
    for row in result:
      app_name = row.get("app_name", "Unknown")
      doc_id = row.get("document_id", "Unknown")
      key = (app_name, doc_id)

      if key not in grouped_data:
        grouped_data[key] = []

      grouped_data[key].append(row)

    platform_rows = []
    for (app_name, doc_id), records in grouped_data.items():
      platform_rows.append({
        "app_name": app_name,   # You can rename this throughout if needed
        "types": [{
          "doc_id": doc_id,  # Again, rename in UI if needed
          "records": records
        }]
      })

    self.repeating_panel_platforms.items = platform_rows