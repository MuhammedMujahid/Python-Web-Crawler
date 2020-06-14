from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

PATH = '/home/muhammed/Downloads/chromedriver_linux64/chromedriver'
driver = webdriver.Chrome(PATH)

driver.get("https://www.businessesforsale.com")
print(driver.title)

search = driver.find_element_by_name("keywords")
search.send_keys("test")
search.send_keys(Keys.RETURN) #hits enter

time.sleep(5)

driver.quit()