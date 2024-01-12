import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
  @classmethod
  def setUpClass(cls):
    print("setupClass prints executes test are done")

  @classmethod
  def tearDownClass(cls):
    print("teardownClass executes after test are done")


  # This method is created before every time before running the test
  def setUp(self):
    self.employee_1 = Employee("Diana", "Wangui", 300000)
    self.employee_2 = Employee("John", "Kariuki", 400000)

  def tearDown(self):
    pass 


  # test case for the email method
  def test_email(self):
    self.assertEqual(self.employee_1.email, "Diana.Wangui@gmail.com")
    self.assertEqual(self.employee_2.email, "John.Kariuki@gmail.com")

  # Changing employee first name
    self.employee_1.first_name = "Velmah"
    self.employee_2.first_name = "Solo"

    self.assertEqual(self.employee_1.email, "Velmah.Wangui@gmail.com")
    self.assertEqual(self.employee_2.email, "Solo.Kariuki@gmail.com")

  # Test case for name method
  def test_name(self):
    self.assertEqual(self.employee_1.name, "Diana Wangui")
    self.assertEqual(self.employee_2.name, "John Kariuki")

    # Changing employee first name
    self.employee_1.first_name = "Velmah"
    self.employee_2.first_name = "Solo"

    self.assertEqual(self.employee_1.name, "Velmah Wangui")
    self.assertEqual(self.employee_2.name, "Solo Kariuki")


  # test case for raise amount method for employee pay
  def test_apply_raise(self):
    self.employee_1.apply_raise()
    self.employee_2.apply_raise()

    self.assertEqual(self.employee_1.pay, 315000)
    self.assertEqual(self.employee_2.pay, 420000)

if __name__ == '__main__':
  unittest.main()