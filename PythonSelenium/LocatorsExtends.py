from selenium import webdriver

# in executable_path - have to share browser driver exe path
driver = webdriver.Chrome(executable_path="C:\\Users\\ashut\\Downloads\\Work\\Python\\chromedriver_win32\\chromedriver.exe")
driver.get("https://login.salesforce.com/")
driver.find_element_by_css_selector("#username").send_keys("ashutosh.qa")   #  #ID can use as css selector
driver.find_element_by_css_selector(".password").send_keys("abc123")  # .classname can use as css selector
#driver.find_element_by_css_selector(".password").clear()
driver.find_element_by_link_text("Forgot Your Password?").click()
driver.find_element_by_xpath("//a[text()='Cancel']").click()   # text can also be used to identify xpath

print(driver.find_element_by_xpath("//form[@name='login']/div[1]/label").text)
print(driver.find_element_by_css_selector("form[name='login'] label:nth-child(3)").text)