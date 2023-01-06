import pytest
@pytest.mark.parametrize("username,password",[("admin","123hcl"),("guest","123hcl")])
def test_login(username,password):
    if((username=="admin" and password=="123hcl") or (username=="guest" and password=="123hcl")):
        assert True
    else:
        assert False
@pytest.mark.parametrize("price",[200,300,400,90,50,150])
def test_purchase(price):
    if(price>100):
        print("pass")
    else:
        print("fail")
def test_logout():
    print("checkout")
