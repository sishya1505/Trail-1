from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = "F:\Software\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www.techwithtim.net/")
print(driver.title)

search = driver.find_element_by_id("search")
search.send_keys("TExt")
search.send_keys(Keys.ENTER)

# to bring the webpage's entire source code = print(driver.page_source)

try:
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "main"))
    )
    print(main.text)
except:
    driver.quit()


driver.quit()
 