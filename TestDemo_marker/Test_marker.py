import pytest
import sys
@pytest.mark.s1
def test_log():
    print("login")
@pytest.mark.r
def test_mul():
    print("addition")
@pytest.mark.skip
def test_sign():
    print("signing")
@pytest.mark.s2
def test_out():
    print("logout")
@pytest.mark.skipif(sys.version_info>(3,7),reason="will execute above version")
def test_demo():
    print("demo class")