# PyTest is Unit testing framework in Python just like TestNG/JUnit in Java
# Any PyTest file should start with test_ OR end with _test
# Any code should wrapped in Method only, PyTest method name should start with test
import pytest


@pytest.mark.sanity
@pytest.mark.skip # to skip any specific method
def test_firstProgram():
    msg = "Hello"
    assert msg == "Hi", "Message validation Failed"


def test_smoke():
    a = 4
    b = 6
    assert a+2 == 6, "Addition result failed"