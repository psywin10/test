import unittest
from main import greet, calculate_sum

class TestMain(unittest.TestCase):
    def test_greet(self):
        self.assertEqual(greet("Manus"), "Olá, Manus!")

    def test_calculate_sum(self):
        self.assertEqual(calculate_sum(2, 3), 5)

if __name__ == '__main__':
    unittest.main()
