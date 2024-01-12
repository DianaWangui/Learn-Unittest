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
    self.assertEqual(calc.mul(3, 5), 15)
    self.assertEqual(calc.mul(-1, 5), -5)
    self.assertEqual(calc.mul(-3, -3), 9)
    self.assertEqual(calc.mul(0, 1), 0)

  def test_div(self):
    self.assertEqual(calc.div(2, 2), 1)
    self.assertEqual(calc.div(-1, -1), 1)
    self.assertEqual(calc.div(-3, 3), -1)
    self.assertEqual(calc.div(5, 2), 2.5)
    
    with self.assertRaises(ValueError):
      calc.div(10, 0)
    
if __name__ == '__main__':
  unittest.main()