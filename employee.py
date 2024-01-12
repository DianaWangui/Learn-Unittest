"""Class to create employee names and emails."""

raise_amount = 1.05

class Employee:
  def __init__(self, first_name, last_name, pay):
    self.first_name = first_name
    self.last_name = last_name
    self.pay = pay

  @property
  def email(self):
    return "{}.{}@gmail.com".format(self.first_name, self.last_name)
  
  @property
  def name(self):
    return "{} {}".format(self.first_name, self.last_name)
  
  def apply_raise(self):
    self.pay = int(self.pay * raise_amount)
