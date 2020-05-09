from selenium import webdriver

# in executable_path - have to share browser driver exe path
driver = webdriver.Chrome(executable_path="C:\\Users\\ashut\\Downloads\\Work\\Python\\chromedriver_win32\\chromedriver.exe")
# driver = webdriver.Firefox(executable_path="C:\\Users\\ashut\\Downloads\\Work\\Python\\geckodriver-v0.26.0-win64\\geckodriver.exe")
# driver = webdriver.Ie(executable_path="C:\\Users\\ashut\\Downloads\\Work\\Python\\IEDriverServer_x64_3.150.1\\IEDriverServer.exe")



driver.get("https://www.selenium.dev/")  # get method to hit URL on browser
print(driver.title)
print(driver.current_url)
driver.get("https://www.selenium.dev/downloads/")
driver.maximize_window()
driver.back()
driver.refresh()




driver.close()