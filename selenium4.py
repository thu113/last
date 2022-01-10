from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

path = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(path)
driver.get("https://vi-vn.facebook.com/")
try:
    driver.implicitly_wait(8)
    #driver.find_element(By.XPATH,"//*[text()='Tạo tài khoản mới']").click()
    driver.find_element(By.CSS_SELECTOR,"div._6ltg>a").click()
    driver.find_element(By.NAME,"lastname").send_keys("Vo")
    driver.find_element(By.NAME,"firstname").send_keys("Thu")
    driver.find_element(By.NAME,"reg_email__").send_keys("Thu@gmail.com")
    driver.find_element(By.NAME,"reg_email_confirmation__").send_keys("Thu@gmail.com")
    driver.find_element(By.NAME,"reg_passwd__").send_keys("a1234568910")
    day = Select(driver.find_element(By.NAME,"birthday_day"))
    day.select_by_visible_text("18")

    month = Select(driver.find_element(By.NAME,"birthday_month"))
    month.select_by_index(9)
    year = Select(driver.find_element(By.NAME, "birthday_year"))
    year.select_by_visible_text("2001")
    driver.find_element(By.XPATH,"//label[text()='Nữ']").click()
    driver.find_element(By.NAME,"websubmit").click()
except Exception as ex:
    print(ex)

driver.close()