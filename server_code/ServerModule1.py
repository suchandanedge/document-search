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
      "order_number": "SOH Clear 2.3.25",
      "line_no": "1",
      "item_id": "101151",
      "displayname": "Doodles x CAMP Playing Cards",
      "ship_qty": "12",
      "ship_date": "2025-02-03",
      "posted_at": "None",
      "type": "Order",
      "platform": "Mainfreight"
    },
    {
      "order_number": "SOH Clear 2.3.25",
      "line_no": "1",
      "item_id": "101151",
      "displayname": "Doodles x CAMP Playing Cards",
      "ship_qty": "2",
      "ship_date": "2025-02-03",
      "posted_at": "None",
      "type": "Invoice",
      "platform": "Mainfreight"
    },
    {
      "order_number": "SOH Clear 2.3.25",
      "line_no": "1",
      "item_id": "101151",
      "displayname": "Doodles x CAMP Playing Cards",
      "ship_qty": "1",
      "ship_date": "2025-02-03",
      "posted_at": "None",
      "type": "Capture",
      "platform": "NetSuite"
    },
    {
      "order_number": "SOH Clear 2.3.25",
      "line_no": "1",
      "item_id": "101151",
      "displayname": "Doodles x CAMP Playing Cards",
      "ship_qty": "1",
      "ship_date": "2025-02-03",
      "posted_at": "None",
      "type": "Order",
      "platform": "Mainfreight"
    },
    {
      "order_number": "SOH Clear 2.3.25",
      "line_no": "1",
      "item_id": "101151",
      "displayname": "Doodles x CAMP Playing Cards",
      "ship_qty": "1",
      "ship_date": "2025-02-03",
      "posted_at": "None",
      "type": "Invoice",
      "platform": "Mainfreight"
    }
    ]
    return result
  except Exception as e:
    return {"error": str(e)}
