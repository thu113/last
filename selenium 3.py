from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import csv
path = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(path)

driver.get("https://lms.ou.edu.vn/")

#driver.find_element(By.CSS_SELECTOR,"section.about>p>a.main-btn").click()
driver.find_element(By.XPATH,"//*[@id='about']/div[1]/div/div[1]/div/a[1]").click()
driver.find_element(By.XPATH,"//*[@id='region-main']/div/div/div/div/form/div[3]/button").click()
he =  Select (driver.find_element(By.NAME,"form-usertype"))
he.select_by_index(0)

with open('TaiKhoan.csv', newline='') as f:
    reader = csv.DictReader(f)
    for r in reader:
        u = r["user"]
        p = r["password"]
driver.find_element(By.NAME,"form-username").send_keys(u)
driver.find_element(By.NAME,"form-password").send_keys(p)
driver.find_element(By.XPATH,"//*[@id='login_form']/div[4]/div/button").click()
driver.implicitly_wait(6)
g = driver.find_elements(By.CSS_SELECTOR,'.dashboard-card .course-info-container .align-items-start')

for i in g:
    print(i.find_element(By.TAG_NAME,"a").text)


driver.close()

