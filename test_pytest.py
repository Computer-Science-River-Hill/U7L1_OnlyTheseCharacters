import main    # The code to test

def test_One():
    assert main.only([1,2,3,4,5],1,3) == False

def test_Two():
    assert main.only([1,4,1,4,1],1,4) == True

def test_Three():
    assert main.only([1,4,1,5,1],1,4) == False

def test_Four():
    assert main.only([2,8,8,2,8],2,8) == True
