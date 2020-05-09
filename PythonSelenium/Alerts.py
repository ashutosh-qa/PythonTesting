from selenium import webdriver

validateText = "Ashutosh"
driver = webdriver.Chrome(executable_path="C:\\Users\\ashut\\Downloads\\Work\\Python\\chromedriver_win32\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.find_element_by_id("name").send_keys(validateText)
driver.find_element_by_id("alertbtn").click()
alert = driver.switch_to.alert
alerttext = alert.text
assert validateText in alerttext


alert.accept()

driver.find_element_by_id("confirmbtn").click()
alert = driver.switch_to.alert
alert.dismiss()

