from selenium import webdriver
PATH = '/home/muhammed/Downloads/chromedriver_linux64/chromedriver'
driver = webdriver.Chrome(PATH)

driver.get("https://www.businessesforsale.com")
print(driver.title)
driver.quit()