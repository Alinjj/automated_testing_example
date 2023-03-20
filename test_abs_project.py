




def test_abs():
    assert abs(-42) == 42, "Should be absolute value of number"
def test_abs1():
    assert abs(-42) == -42, "Should be absolute value of number"

if __name__ == "__main__":
    test_abs()
    test_abs1()
    print('All tests passed')