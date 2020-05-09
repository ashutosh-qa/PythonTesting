import time

from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path="C:\\Users\\ashut\\Downloads\\Work\\Python\\chromedriver_win32\\chromedriver.exe")
driver.get("https://www.familysearch.org/en/")
driver.maximize_window()
# ActionChains are classes which are used to perform advance interactions e.g.
# click on menu and then sub-menu. We have to use the methods present in this class to perform the actions

action = ActionChains(driver)
driver.find_element_by_css_selector("button[aria-controls='search']")
time.sleep(1)
action.move_to_element(driver.find_element_by_css_selector("button[aria-controls='search']")).click().perform()
#here it is mandatory to put/set perform bcoz to complete the action, perform method is required
time.sleep(4)
time.sleep(1)
driver.find_element_by_css_selector("a[data-test='genealogies']").click()
print(driver.title)
assert "https://www.familysearch.org/search/family-trees" == driver.current_url


# #Double Click
driver.get("https://chercher.tech/practice/practice-pop-ups-selenium-webdriver")
action.double_click(driver.find_element_by_id("double-click")).perform()

alert = driver.switch_to.alert
assert "You double clicked me!!!, You got to be kidding me" == alert.text

alert.accept()


