from src.basics.task_0.task_0 import add

def test_add_positive():
    assert add(2, 3) == 5

def test_add_negative():
    assert add(-1, 1) == 0

def test_add_zero():
    assert add(0, 0) == 0

test_add_positive()
test_add_negative()
test_add_zero()