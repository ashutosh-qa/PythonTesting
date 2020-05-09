from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\Users\\ashut\\Downloads\\Work\\Python\\chromedriver_win32\\chromedriver.exe")
driver.get("https://the-internet.herokuapp.com/windows")

driver.find_element_by_link_text("Click Here").click()
# Window_handles is the method that will get all the windows opened by selenium, this is list. like ("parentid", "childid")
# Selenium by default open patent window, i.e. [0], for child window its [1]
childwindow = driver.window_handles[1]
driver.switch_to.window(childwindow)

print(driver.find_element_by_tag_name("h3").text)
driver.close()

driver.switch_to.window(driver.window_handles[0])
assert "Opening a new window" == driver.find_element_by_tag_name("h3").text
driver.close()