import pytest

#Make sure to start your class names with word Test (uppercase T) and your method names with test (lowercase T).
from PyTest.BaseClass import BaseClass


@pytest.mark.usefixtures("dataLoad")
class Testexample2(BaseClass):

    def test_usecreateddata(self, dataLoad):
        print("Here using created data from conftest - dataLoad")
        log = self.getLogger()
        log.info(dataLoad[0])
        log.info(dataLoad[1])
        print(dataLoad[2])

