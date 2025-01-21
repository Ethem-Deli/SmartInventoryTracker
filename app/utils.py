from app.database import get_connection
from app.models import update_inventory_item

def fifo_management(item_id, sold_quantity):
    connection = get_connection()
    if not connection:
        print("Failed to connect to the database.")
        return
    cursor = connection.cursor()
    try:
        cursor.execute("SELECT quantity FROM inventory WHERE id = :1", [item_id])
        result = cursor.fetchone()
        if not result:
            print(f"Item {item_id} not found.")
            return
        current_quantity = result[0]
        if current_quantity >= sold_quantity:
            update_inventory_item(item_id, current_quantity - sold_quantity)
        else:
            print("Not enough stock!")
    finally:
        cursor.close()
        connection.close()

