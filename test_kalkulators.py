import unittest
from kalkulators import saskaitit

class TestKalkulators(unittest.TestCase):

    def test_saskaitit_pozitivus(self):
        self.assertEqual(saskaitit(2, 3), 5)
        
    def test_saskaitit_negativus(self):
        self.assertEqual(saskaitit(-1, -1), -2)
        
if __name__ == "__main__":
    unittest.main()