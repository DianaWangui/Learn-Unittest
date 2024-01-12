import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
  def test_email(self):
    employee_1 = Employee("Diana", "Wangui", 300000)
    employee_2 = Employee("John", "Kariuki", 400000)

    self.assertEqual(employee_1.email, "Diana.Wangui@gmail.com")
    self.assertEqual(employee_2.email, "John.Kariuki@gmail.com")

    employee_1.first_name = "Velmah"
    employee_2.first_name = "Solo"

    self.assertEqual(employee_1.email, "Velmah.Wangui@gmail.com")
    self.assertEqual(employee_2.email, "Solo.Kariuki@gmail.com")

  def test_name(self):
    employee_1 = Employee("Diana", "Wangui", 300000)
    employee_2 = Employee("John", "Kariuki", 400000)

    self.assertEqual(employee_1.name, "Diana Wangui")
    self.assertEqual(employee_2.name, "John Kariuki")

  def test_apply_raise(self):
    employee_1 = Employee("Diana", "Wangui", 50000)
    employee_2 = Employee("John", "Kariuki", 60000)

    employee_1.apply_raise()
    employee_2.apply_raise()

    self.assertEqual(employee_1.pay, 52500)
    self.assertEqual(employee_2.pay, 63000)

if __name__ == '__main__':
  unittest.main()