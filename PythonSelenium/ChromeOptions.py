from selenium import webdriver


#Chrome Options is the class providing various options
# Refer - https://www.programcreek.com/python/example/100025/selenium.webdriver.ChromeOptions

chrome_options = webdriver.ChromeOptions()
# Some examples
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("headless")
chrome_options.add_argument("--ignore-certificate-errors")

driver = webdriver.Chrome(executable_path="C:\\Users\\ashut\\Downloads\\Work\\Python\\chromedriver_win32\\chromedriver.exe", options=chrome_options)
driver.get("https://rahulshettyacademy.com/angularpractice/")

print(driver.current_url)