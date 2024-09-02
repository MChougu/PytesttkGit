import time
from selenium import webdriver
###It is because of line no 30 Except:
from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By

driver= webdriver.Chrome()
driver.get("https://automation.credence.in/shop")

# # Click on Register
# driver.find_element(By.XPATH,"//a[normalize-space()='Register']").click()
# driver.find_element(By.ID,"name").send_keys("MSD")
# driver.find_element(By.ID,"email").send_keys("mcreds@Cred.in")
# driver.find_element(By.NAME,"password").send_keys("Cred.Cred.in")
# driver.find_element(By.NAME,"password_confirmation").send_keys("Cred.Cred.in")
# time.sleep(4)
# print("Before reg Title of page is:", driver.title)
# # Click on registration button to complete
# driver.find_element(By.XPATH,"//button[@type='submit']").click()
# print("After reg Title of page is:",driver.title)
# ###39:00 page title error to Dev
# ## Validate the Registration page
# # if driver.title == "CredKart":
# #     print("registration is completed")
# # else:
# #     print("registration is NOT completed")
# ### we have to handle EXCEPTIONS here title page is same
# try:
#     driver.find_element(By.XPATH,"//h2[normalize-space()='CredKart']")
#     print("registration is completed")
# except (NoSuchElementException, TimeoutException):
#     print("registration is Failed")
# ### 48:00 If needed then only do exception handling else do.



# Click on Login
driver.find_element(By.XPATH, "//a[normalize-space()='Login']").click()
driver.find_element(By.ID,"email").send_keys("Credence11@credence.in")
driver.find_element(By.ID,"password").send_keys("Credence@123")
# untick, tick check BOX
driver.find_element(By.XPATH,"//input[@name='remember']").is_selected()
time.sleep(2)
# driver.find_element(By.XPATH,"//input[@name='remember']").is_enabled()
time.sleep(2)

# Click on Login Button
driver.find_element(By.XPATH,"//button[@type='submit']").click()
# check Logout option
driver.find_element(By.XPATH,'//*[@id="navbar"]/ul[2]/li[3]/a').click()
time.sleep(3)

# Click on Login
driver.find_element(By.XPATH,'//*[@id="navbar"]/ul[2]/li[3]/ul/li/a').click()
time.sleep(4)
# Click on Login
