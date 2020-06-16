from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


PATH = '/home/muhammed/Downloads/chromedriver_linux64/chromedriver'
driver = webdriver.Chrome(PATH)

driver.get("https://www.businessesforsale.com")
print(driver.title)

search = driver.find_element_by_name("keywords")
search.send_keys("test")
search.send_keys(Keys.RETURN) #hits enter

# try:
# 	main = WebDriverWait(driver, 10).until(
# 		EC.presence_of_element_located((By.NAME, "")))
time.sleep(5)

# FINDING ELEMENT BY XPATH

page = driver.find_element_by_xpath('//a[@href="https://www.businessesforsale.com/search/businesses-for-sale-2?Keywords=test"]').click()
time.sleep(5)

# for pages in page:
# 	print(pages.get_attribute("href"))

# print(page)

# FINDING ELEMENT WITH PARTIAL LINK

# subject = driver.find_element_by_partial_link_text("https://www.businessesforsale.com/search/businesses-for-sale-2?Keywords=test")

driver.quit()