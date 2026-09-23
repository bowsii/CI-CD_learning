from factorial import factorial

def test_factorial0():
    assert factorial(0) == 1

def test_factorial1():
    assert factorial(1) == 1        

def test_factorial5():
    assert factorial(5) == 120  

def test_factorial_negative():
    try:
        factorial(-1)
    except ValueError as e:
        assert str(e) == "Factorial is not defined for negative numbers."
    else:
        assert False, "Expected ValueError for negative input"