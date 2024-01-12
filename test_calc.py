import unittest
import calc

class TestCalc(unittest.TestCase):
  def test_add(self):
    self.assertEqual(calc.add(3, 5), 8)
    self.assertEqual(calc.add(-1, 5), 4)
    self.assertEqual(calc.add(-3, -3), -6)
    self.assertEqual(calc.add(-1, 1), 0)

  def test_sub(self):
    self.assertEqual(calc.sub(3, 5), -2)
    self.assertEqual(calc.sub(-1, 5), -6)
    self.assertEqual(calc.sub(-3, -3), 0)
    self.assertEqual(calc.sub(5, 1), 4)


  def test_mul(self):
    self.assertEqual(calc.mul(3, 5), 8)
    self.assertEqual(calc.mul(-1, 5), 4)
    self.assertEqual(calc.mul(-3, -3), -6)
    self.assertEqual(calc.mul(-1, 1), 0)

    
