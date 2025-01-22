from app.database import get_connection
from app.models import update_inventory_item

# FIFO Management with improved comments
def fifo_management(item_id, sold_quantity):
    """
    Applies First-In-First-Out (FIFO) logic to manage inventory.

    Parameters:
    - item_id (int): ID of the inventory item.
    - sold_quantity (int): Quantity sold to deduct.

    Returns:
    - None. Updates the database directly.
    """
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

# Coloring inventory items based on price range
def get_inventory_colored_by_price():
    """
    Retrieves inventory items with a color code based on price ranges.

    Returns:
    - List of items with associated colors (e.g., green, yellow, red).
    """
    connection = get_connection()
    if not connection:
        print("Failed to connect to the database.")
        return []
    cursor = connection.cursor()
    try:
        cursor.execute("SELECT id, product_name, price FROM inventory")
        items = cursor.fetchall()
        colored_items = []
        for item in items:
            color = "green" if item[2] < 500 else "yellow" if item[2] < 1000 else "red"
            colored_items.append({"id": item[0], "product_name": item[1], "price": item[2], "color": color})
        return colored_items
    finally:
        cursor.close()
        connection.close()
