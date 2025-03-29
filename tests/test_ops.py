from src.math_ops import add,subtract

def test_add():
    assert add(2,3)==5
    assert add(5,1)==6
    assert add(3,2)==5

def test_sub():
    assert subtract(99,3)==96
    assert subtract(99,1)==98
