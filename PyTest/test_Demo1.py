# PyTest is Unit testing framework in Python just like TestNG/JUnit in Java
# Any PyTest file should start with test_ OR end with _test
# Any code should wrapped in Method only, PyTest method name should start with test
# -s logs in output
# -v for more info metadata
# -k stands for method name execution
# Can mark (tag) tests @pytest.mark.sanity and then run with -m

import pytest


@pytest.mark.sanity
def test_firstProgram():
    print("Hello")


@pytest.mark.xfail
def test_smoke():
    print("Good Morning")

#here can define without self as its not under class
def test_crossBrowser(crossBrowser):
    print(crossBrowser[1])
