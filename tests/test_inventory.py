import unittest
from app.models import add_inventory_item, get_inventory_low_stock

class TestInventory(unittest.TestCase):
    def test_add_inventory_item(self):
        add_inventory_item("Test Product", 5, 100, "Batch-Test")
        # Add assertions for validation if needed

    def test_low_stock(self):
        low_stock_items = get_inventory_low_stock(10)
        self.assertIsInstance(low_stock_items, list)

if __name__ == "__main__":
    unittest.main()
