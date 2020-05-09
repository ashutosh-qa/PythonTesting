import time

from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\Users\\ashut\\Downloads\\Work\\Python\\chromedriver_win32\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/seleniumPractise/")

listOfTotalItems= []
BeforeSearch = (driver.find_elements_by_xpath("//div[@class='product-action']/button/parent::div/parent::div/h4"))
for BS in BeforeSearch:
    listOfTotalItems.append(BS.text)
print(listOfTotalItems)


driver.find_element_by_css_selector("input.search-keyword").send_keys("ber")
time.sleep(1)
filteredItems = []
AfterSearch = (driver.find_elements_by_xpath("//div[@class='product-action']/button/parent::div/parent::div/h4"))
for AS in AfterSearch:
    filteredItems.append(AS.text)
print(filteredItems)

for i in filteredItems:
    assert i in listOfTotalItems









