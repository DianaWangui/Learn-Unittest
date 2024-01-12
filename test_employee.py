import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
  def test_email(self):
    employee_1 = Employee("Diana", "Wangui", 300,000)
    employee_2 = Employee("John", "Kariuki", 400, 000)

    self.assertEqual(employee_1.email("Diana.Wangui@gmail.com"))
    self.assertEqual(employee_2.email("John.Kariuki@gmail.com"))

  def test_name(self):
    employee_1 = Employee("Diana", "Wangui", 300,000)
    employee_2 = Employee("John", "Kariuki", 400,000)

    self.assertEqual(employee_1.name("Diana Wangui"))
    self.assertEqual(employee_2.email("John Kariuki"))

  def apply_raise(self):
    employee_1 = Employee("Diana", "Wangui", 300,000)
    employee_2 = Employee("John", "Kariuki", 400,000)

    self.assertEqual(employee_1.apply_raise()303,150)
    self.assertEqual(employee_2.apply_raise(404,200))