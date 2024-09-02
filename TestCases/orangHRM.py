import time

from selenium import webdriver
from selenium.webdriver.common.by import By
driver= webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(4)
##enter username
# driver.find_element(By.NAME,"username").send_keys("Admin")
driver.find_element(By.XPATH,"//input[@placeholder='Username']").send_keys("Admin")

#Enter pswd
# driver.find_element(By.NAME,"").send_keys("admin123")
driver.find_element(By.XPATH,"//input[@placeholder='Password']").send_keys("admin123")
time.sleep(3)
#click on login
driver.find_element(By.XPATH, "//button[@type='submit']").click()
time.sleep(5)
# LOgout
## Click to dropdown
driver.find_element(By.XPATH,"//span[@class='oxd-userdropdown-tab']").click()
time.sleep(2)
#Click on Logout
driver.find_element(By.XPATH,"//a[normalize-space()='Logout']")
time.sleep(2)
##### You can explore TestCaseStudio--- selectorhubs--- just add in your browser.


