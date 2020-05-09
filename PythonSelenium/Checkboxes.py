from selenium import webdriver

# in executable_path - have to share browser driver exe path
driver = webdriver.Chrome(executable_path="C:\\Users\\ashut\\Downloads\\Work\\Python\\chromedriver_win32\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

checkboxes = driver.find_elements_by_xpath("//input[@type='checkbox']")
print(len(checkboxes))

for checkbox in checkboxes:
    if checkbox.get_attribute("value") == "Option 2":
        checkbox.click()
        assert checkbox.is_selected()



radiobuttons = driver.find_elements_by_name("radioButton")
radiobuttons[2].click()
assert radiobuttons[2].is_selected()


# Hide Show

assert driver.find_element_by_id("displayed-text").is_displayed()
driver.find_element_by_id("hide-textbox").click()
assert not driver.find_element_by_id("displayed-text").is_displayed()
print("Test Passed")
driver.close()
