import unittest
from app.database import get_connection

class TestDatabase(unittest.TestCase):
    def test_connection(self):
        connection = get_connection()
        self.assertIsNotNone(connection)

if __name__ == "__main__":
    unittest.main()
