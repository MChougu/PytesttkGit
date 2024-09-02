import random

from selenium import webdriver
import pytest
import time
from selenium.webdriver.common.by import By


@pytest.mark.regression
def test_Amazon_GetRandom_Items_001():
    driver=webdriver.Chrome()
    driver.get("https://www.amazon.in/")
    driver.find_element(By.XPATH,"//input[@id='twotabsearchtextbox']").send_keys("women kurties")
    driver.find_element(By.XPATH, "//input[@id='nav-search-submit-button']").click()
    l=len(driver.find_elements(By.XPATH,'//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div'))
    print(l)
    RandomNum =random.randint(1, l+1)
    driver.find_element(By.XPATH,'//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div[' + str(
                                                 RandomNum) + "]").click()
    time.sleep(4)
    print("Page Title is",driver.title)
    print("selected Item No is: ",RandomNum)

# @pytest.mark.regression
def test_Amazon_Items_002():
    driver = webdriver.Chrome()
    driver.get("https://www.amazon.in/")
    driver.find_element(By.XPATH, "//input[@id='twotabsearchtextbox']").send_keys("women kurties")
    driver.find_element(By.XPATH, "//input[@id='nav-search-submit-button']").click()
    l = len(driver.find_elements(By.XPATH, '//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div'))
    print(l)
    secondOpt= 2
    driver.find_element(By.XPATH, '//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div[' + str(
            secondOpt) + "]").click()
    time.sleep(4)
    print(driver.title)

    print("fixOption is", secondOpt)

    # aHandles=driver.window_handles
    # print("Print All Windows", aHandles)
    # for i in aHandles:
    #     driver.switch_to.window(i)
    #     print(driver.title)
    # eleText=driver.find_element(By.XPATH,'//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div[4]/div/div/div/div/span/div/div/div[2]/div[1]/h2/a/span/text()')
    # print("h2content is : ", eleText.get_attribute('innerHTML'))
    # for r in range(1, l + 1):
    #     optionSa = driver.find_element(By.XPATH,
    #                                          '//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div[' + str(
    #                                              r) + "]").text
    #     print(optionSa)
    # #
    # #     aNum = random.randint(1, 59)
    # // *[ @ id = "search"] / div[1] / div[1] / div / span[1] / div[1] / div[
    #     4] / div / div / div / div / span / div / div / div[2] / div[1] / h2 / a / span / text()
    # // *[ @ id = "search"] / div[1] / div[1] / div / span[1] / div[1] / div[
    #     4] / div / div / div / div / span / div / div / div[2] / div[1] / h2 / a / span
    #     #'//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div[4]').click()
    # aNum = random.randint(1, 59)
    # print("any random no is:", aNum)

