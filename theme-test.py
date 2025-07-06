a = 10
b = 5


if a > b:
  print("a is greater than b")

while a > 0:
  print(a)
  a -= 1


def add(x, y):
  """Function to add two numbers."""
  return x + y


def subtract(x, y):
  """Function to subtract two numbers."""
  return x - y


class Calculator:
  """A simple calculator class."""

  def __init__(self):
    pass

  def multiply(self, x, y):
    """Function to multiply two numbers."""
    return x * y

  def divide(self, x, y):
    """Function to divide two numbers."""
    if y == 0:
      raise ValueError("Cannot divide by zero.")
    return x / y


my_list = [{
    "name": "example",
    "value": 42
}]
my_list.append({"name": "new_item", "value": 100})
variable = "This is a test string."
number = 3.14
