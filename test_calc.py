import unittest
import calc

class TestCalc(unittest.TestCase):
  def test_add(self):
    self.assertEqual(calc.add(3, 5), 8)
    self.assertEqual(calc.add(-1, 5), 4)
    self.assertEqual(calc.add(-3, -3), -6)
    self.assertEqual(calc.add(-1, -1), 2)
    
