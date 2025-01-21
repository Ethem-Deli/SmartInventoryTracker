from app.models import add_inventory_item, add_employee, create_tables, get_inventory_low_stock, get_fastest_selling_item

def main():
    """Main application logic."""
    create_tables()  # Ensures database tables are created before operations.
    print("Welcome to Smart Inventory Tracker")

    # Example: Adding inventory items
    add_inventory_item("Laptop", 10, 1200, "Batch-001")
    add_inventory_item("Phone", 25, 800, "Batch-002")

    # Example: Adding employees
    add_employee("John Doe", "john.doe@example.com", "Sales")
    add_employee("Jane Smith", "jane.smith@example.com", "Marketing")

    # Example: Checking for low-stock items
    low_stock_items = get_inventory_low_stock(15)
    if low_stock_items:
        print("Low stock items:")
        for item in low_stock_items:
            print(item)

    # Example: Fetching the fastest-selling item
    fastest_selling = get_fastest_selling_item()
    if fastest_selling:
        print("Fastest selling item:", fastest_selling)

if __name__ == "__main__":
    main()
