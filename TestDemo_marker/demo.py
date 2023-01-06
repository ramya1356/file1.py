import pytest
#class Testdemo:
@pytest.mark.parametrize("data",[6,7,9])
def test_nogt(data):
    if(data>5):
        assert True
    else:
        assert False