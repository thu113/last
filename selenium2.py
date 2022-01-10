from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
path = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(path)

driver.get("https://vnexpress.net/")
print(driver.title)
#print(driver.page_source)
arti = driver.find_elements(By.CSS_SELECTOR,"article.item-news")
for i in arti:
    try:
         t = i.find_element(By.TAG_NAME,"h3")
         print(t.text)
         d = i.find_element(By.TAG_NAME,"p")
         print(d.text)
         print(t.find_element(By.TAG_NAME,"a").get_attribute("href"))
         print("============")
    except NoSuchElementException:
        print("error")
driver.close()

