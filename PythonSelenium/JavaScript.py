from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\Users\\ashut\\Downloads\\Work\\Python\\chromedriver_win32\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element_by_name("name").send_keys("Ashutosh")
print(driver.find_element_by_name("name").get_attribute("value"))  #get attribute is inheritted from java script DOM

# Execute Script - To pass pure Java script command, selenium giving its control to jS, whatever you pass in this argument
print(driver.execute_script('return document.getElementsByName("name")[0].value'))

# ----------------------------------------------------------------
shopButton = driver.find_element_by_css_selector("a[href*='shop']")
driver.execute_script("arguments[0].click();", shopButton)  # Here shopButton is at 0th index so passing argument as 0

# Selenium doesn't support scrolling, thru JS can do scrolling
driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")


