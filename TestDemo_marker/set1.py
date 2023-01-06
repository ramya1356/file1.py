import pytest
@pytest.mark.parametrize("n,r",[(2,4),(1,1),(5,25)])
def test_sq(n,r):
    assert n*n==r
@pytest.mark.parametrize('username,password',[("hcl",123),("wip",456),("tcs",789)])
def test_det(username,password):
    print(username)
    print(password)
