import unittest
from app.models import add_employee

class TestEmployees(unittest.TestCase):
    def test_add_employee(self):
        add_employee("Test Employee", "test@example.com", "Testing")
        # Add assertions for validation if needed

if __name__ == "__main__":
    unittest.main()
