import pytest
@pytest.fixture(scope="session",autouse=True)
def log():
    print("entering")
    print("login")
    yield
    print("logout")

