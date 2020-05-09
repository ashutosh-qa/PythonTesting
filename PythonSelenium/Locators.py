from selenium import webdriver

# in executable_path - have to share browser driver exe path
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="C:\\Users\\ashut\\Downloads\\Work\\Python\\chromedriver_win32\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/angularpractice/")
#driver.find_element_by_name("name").send_keys("Ashutosh")
driver.find_element_by_css_selector("input[name='name']").send_keys("Ashutosh")
driver.find_element_by_name("email").send_keys("ashutosh.qa@gmail.com")
driver.find_element_by_id("exampleCheck1").click()

#Select class provides the method to handle the options in drop down

dropdown = Select(driver.find_element_by_id("exampleFormControlSelect1"))
dropdown.select_by_visible_text("Female")
dropdown.select_by_index(0)

driver.find_element_by_xpath("//input[@type='submit']").click()

print(driver.find_element_by_css_selector("div[class*='alert-success']").text)   #CSS regular expresssion
print(driver.find_element_by_xpath("//div[contains(@class,'alert-success')]").text)   #xpath regular expresssion

message = driver.find_element_by_xpath("//div[contains(@class,'alert-success')]").text
assert "success" in message
#driver.close()