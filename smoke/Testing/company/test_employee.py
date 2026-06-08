import pytest
from employee import Employee as Em

@pytest.fixture
def employee():
    ast = Em("Prince", "Agyei", 40000)
    return ast

def test_give_default_raise(employee):
    ast = employee.employee_raise()
    assert ast == "Prince Agyei has a salary of 45000"

def test_give_custom_raise(employee):
    ces = employee.employee_raise(3000)
    assert ces == "Prince Agyei has a salary of 43000"


