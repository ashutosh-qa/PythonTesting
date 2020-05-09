#Explicit Wait
import time

from selenium import webdriver
#pause the test for few seconds using Time class
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

list = []
list2 = []
driver = webdriver.Chrome(executable_path="C:\\Users\\ashut\\Downloads\\Work\\Python\\chromedriver_win32\\chromedriver.exe")

driver.get("https://rahulshettyacademy.com/seleniumPractise/")
driver.find_element_by_css_selector("input.search-keyword").send_keys("ber")
time.sleep(4)
count =len(driver.find_elements_by_xpath("//div[@class='products']/div"))
assert count == 3
buttons = driver.find_elements_by_xpath("//div[@class='product-action']/button")
#//div[@class='product-action']/button/parent::div/parent::div/h4
for button in buttons:
    list.append(button.find_element_by_xpath("parent::div/parent::div/h4").text)  # In Xpath only, can traverse up like child to parent, not in CSS
    button.click()
print(list)  # it will print all three 'ber' veggie

driver.find_element_by_css_selector("img[alt='Cart']").click()  #Click on Cart image
driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()
#Explicit Wait
wait = WebDriverWait(driver, 8)
wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "promoCode")))

veggies = driver.find_elements_by_css_selector("p.product-name")
for veg in veggies:
    list2.append(veg.text)  # List 2 has list of 'ber' veggie

print(list2)
assert list == list2  # Product selected in Page1 showing in Page 2

originalAmount = driver.find_element_by_css_selector(".discountAmt").text   # Capturing veggie original amount
driver.find_element_by_class_name("promoCode").send_keys("rahulshettyacademy")
driver.find_element_by_css_selector(".promoBtn").click()

wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,"span.promoInfo")))
discountAmount = driver.find_element_by_css_selector(".discountAmt").text # Capturing veggie discount

# If Price decreases on Discount
assert float(discountAmount) < int(originalAmount)   # Both veggies amount are in string so converting into float/int

print(driver.find_element_by_css_selector("span.promoInfo").text)

# Sum of the products in checkout page, matches with Total Amount

amounts = driver.find_elements_by_xpath("//tr/td[5]/p")
sum = 0
for amount in amounts:
    sum = sum + int(amount.text) #32+48+60

print(sum)

totalAmount = int(driver.find_element_by_class_name("totAmt").text)

assert sum == totalAmount
print("---- Test Case Passed----")
driver.close()




















