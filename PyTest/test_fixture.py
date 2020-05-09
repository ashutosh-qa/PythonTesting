# fixtures are used as setup and tier down method for test cases
# conftest file is used to generate fixture and make it available to all test cases in same folder
import pytest


@pytest.mark.usefixtures("setup")  #It will apply to all the methods present in the class
class Testexample:
    def test_fixtureDemo(self):
        print("I am the main TC code")

    def test_fixtureDemo1(self):
        print("I am the main TC code1")

    def test_fixtureDemo2(self):
        print("I am the main TC code2")

    def test_fixtureDemo3(self):
        print("I am the main TC code3")
