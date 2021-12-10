import pytest

class NotInRange(Exception) :
    def __init__(self, message = "Value not in range") :
        self.message =message
        super().__init__(self.message)

def test1_generic() :
    a = 2
    b = 2
    assert a==b

def test2_generic() :
    a = 2
    b = 21
    assert a!=b    

#def test_exception() :
#    a = 5
#    with pytest.raises(ValueError) :
#        if a not in(10,20) :
#            raise NotInRange
           