from selenium import webdriver
import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.service import Service
headless_option = webdriver.ChromeOptions()
headless_option.add_argument("headless")

# def test_reg_ced001():
#     driver=webdriver.Chrome()
#     driver.get("https://credence.in/")
#

@pytest.mark.regression
def test_Credence_006():
    # headless_option = webdriver.ChromeOptions()
    # headless_option.add_argument("headless")
    # driver = webdriver.Chrome(options=headless_option)
    driver=webdriver.Chrome()
    driver.get("https://credence.in/")
    time.sleep(2)
    driver.find_element(By.XPATH, "//img[@src='/website/images/enquiry.png']").click()
                                                                        #//*[@id="thim-body"]/div[3]/a/img').click()
                                                    #//img[@src='/website/images/enquiry.png']").click()
    time.sleep(5)
    l = len(driver.find_elements(By.XPATH, '//*[@id="popupDIv"]/div/p/a'))
                                                           #"//div[@class='quickfinder-description gem-text-output']//p//a"))
    print("length is:", l)
    Contact_Number_List = []
    for r in range(1, l + 1):
        Contact_Number = driver.find_element(By.XPATH,
                                             "//div[@class='quickfinder-description gem-text-output']//p//a[" + str(
                                                 r) + "]").text
        print(Contact_Number)
        Contact_Number_List.append(Contact_Number)
    print(Contact_Number_List)
    mb = "+91 9579064658"  #95790646580"
    if mb in Contact_Number_List:
        print(Contact_Number_List.index(mb))
        assert True
    else:
        assert False
