import pytest


# @Before test
@pytest.fixture(scope="class")
# scope="class" by defining like this, fixture will execute before class and end of class, not before/after every method

def setup():
    print("I am pre-condition test")
    yield  # Yield is just like @aftertest annotation in testNG
    print("I am post-condition test")


# Here under Fixture creating data to use in TCs
@pytest.fixture()
def dataLoad():
    print("Data for TC is created here")
    return ["FirstName", "LastName", "EmailID"]


# How to parameterized in multi browsers
@pytest.fixture(params=[("Chrome", "FName", "LName"), ("Firefox", "FName", "LName"), ("IE", "Name")])
def crossBrowser(request):
    # in request parameter, whatever declared in params, each time one value will pick
    # request is tied to fixture
    return request.param
