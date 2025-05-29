import anvil.server

# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#
def get_db_read_connection():
  pass
@anvil.server.callable
def document_search(order_number):
  order_number_lower = order_number.lower()
  # query = f"""
  #   SELECT 
  #       msd.order_number,
  #       msd.line_no,
  #       msd.item_id,
  #       i.displayname,
  #       msd.ship_qty,
  #       msd.ship_date,
  #       msd.posted_at,
  #   FROM mainfreight.mainfreight_shipment_detail msd 
  #   LEFT OUTER JOIN netsuite.item i ON msd.item_id = i.id::varchar
  #   WHERE LOWER(msd.order_number) = '{order_number_lower}'
  #   ORDER BY msd.line_no
  #   """
  try:
    # conn = get_db_read_connection()
    # conn.db_execute(query)
    # result = conn.db_AllRowJson()
    result = [
          {
            "log_id" : 11322,
            "app_name" : "mainfreight_po",
            "component_name" : "send_orders",
            "function_name" : "send_orders",
            "is_error" : True,
            "status_code" : 404,
            "error_text" : "",
            "document_id" : "11442",
            "log_time" : "2025-05-29T07:37:33.030Z",
            "response" : "{}",
            "payload" : "{\"customer\": {\"code\": \"7346087\"}, \"warehouse\": {\"code\": \"56\"}, \"inwardLines\": [{\"units\": \"5000\", \"lineNo\": \"1\", \"product\": {\"code\": \"74059\"}}], \"inwardReference\": \"11442\", \"inwardReference1\": 18699016, \"receiverReference\": \"\"}",
            "details" : "{}",
            "parent_key" : "11442",
            "system_type" : "",
            "log_date" : "2025-05-29",
            "base_document_id" : "11442",
            "item_name" : "item74059"
          },
          {
            "log_id" : 11345,
            "app_name" : "mainfreight_po",
            "component_name" : "send_orders",
            "function_name" : "send_orders",
            "is_error" : True,
            "status_code" : 404,
            "error_text" : "",
            "document_id" : "11442-1",
            "log_time" : "2025-05-29T07:38:34.192Z",
            "response" : "{}",
            "payload" : "{\"customer\": {\"code\": \"7346087\"}, \"warehouse\": {\"code\": \"56\"}, \"inwardLines\": [{\"units\": \"5000\", \"lineNo\": \"1\", \"product\": {\"code\": \"74060\"}}], \"inwardReference\": \"11442\", \"inwardReference1\": 18699016, \"receiverReference\": \"\"}",
            "details" : "{}",
            "parent_key" : "11442",
            "system_type" : "",
            "log_date" : "2025-05-29",
            "base_document_id" : "11442",
            "item_name" : "item74060"
          },
          {
            "log_id" : 11350,
            "app_name" : "mainfreight_po",
            "component_name" : "send_orders",
            "function_name" : "send_orders",
            "is_error" : True,
            "status_code" : 404,
            "error_text" : "",
            "document_id" : "11442-1",
            "log_time" : "2025-05-29T07:39:01.758Z",
            "response" : "{}",
            "payload" : "{\"customer\": {\"code\": \"7346087\"}, \"warehouse\": {\"code\": \"56\"}, \"inwardLines\": [{\"units\": \"5000\", \"lineNo\": \"1\", \"product\": {\"code\": \"74060\"}}], \"inwardReference\": \"11442\", \"inwardReference1\": 18699016, \"receiverReference\": \"\"}",
            "details" : "{}",
            "parent_key" : "11442",
            "system_type" : "",
            "log_date" : "2025-05-29",
            "base_document_id" : "11442",
            "item_name" : "item74060"
          },
          {
            "log_id" : 11351,
            "app_name" : "mainfreight_po",
            "component_name" : "send_orders",
            "function_name" : "send_orders",
            "is_error" : True,
            "status_code" : 404,
            "error_text" : "",
            "document_id" : "11442-2",
            "log_time" : "2025-05-29T07:39:12.029Z",
            "response" : "{}",
            "payload" : "{\"customer\": {\"code\": \"7346087\"}, \"warehouse\": {\"code\": \"56\"}, \"inwardLines\": [{\"units\": \"5000\", \"lineNo\": \"1\", \"product\": {\"code\": \"74061\"}}], \"inwardReference\": \"11442\", \"inwardReference1\": 18699016, \"receiverReference\": \"\"}",
            "details" : "{}",
            "parent_key" : "11442",
            "system_type" : "",
            "log_date" : "2025-05-29",
            "base_document_id" : "11442",
            "item_name" : "item74061"
          }
    ]
    return result
  except Exception as e:
    return {"error": str(e)}
