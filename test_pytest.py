import main    # The code to test

def test_one():
    assert main.only([1,2,3,4,5],1,3) == False

def test_two():
    assert main.only([1,4,1,4,1],1,4) == True

def test_three():
    assert main.only([1,4,1,5,1],1,4) == False

def test_four():
    assert main.only([2,8,8,2,8],2,8) == True
