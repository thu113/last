from selenium import webdriver
from selenium.webdriver.common.by import By

path = "C:\Program Files (x86)\chromedriver.exe"
kw = input("Nhập vào từ khóa: ")
driver = webdriver.Chrome(path)
driver.get("https://www.google.com.vn/?hl=vi")

inp = driver.find_element(By.NAME,"q")
inp.send_keys(kw)
inp.submit()
re = driver.find_elements(By.CSS_SELECTOR,"div.g")
for i in re:
  content = i.find_element(By.TAG_NAME,"a")
  print(content.text)
  print(content.get_attribute("href"))
  print("===============")

driver.close()