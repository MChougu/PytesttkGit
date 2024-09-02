# # import pytest
# # from selenium import webdriver
# # from selenium.webdriver.common.by import By
# # from selenium.webdriver.support.ui import WebDriverWait
# # from selenium.webdriver.support import expected_conditions as EC
# #
# # @pytest.fixture
# # def driver():
# #     driver = webdriver.Chrome()  # or another driver
# #     driver.get('https://www.youtube.com/')
# #     yield driver
# #     driver.quit()
# #
# # def test_youtube_sign_in(driver):
# #     wait = WebDriverWait(driver, 10)
# #
# #     # Example of waiting for an element to be clickable and then clicking
# #     sign_in_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="buttons"]/ytd-button-renderer/yt-button-shape/a/div[2]')))
# #     sign_in_button.click()
# #
# #     # Example of handling a possible overlay or popup
# #     try:
# #         overlay = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[@class="overlay"]')))
# #         overlay_close_button = overlay.find_element(By.XPATH, './/button[@class="close"]')
# #         overlay_close_button.click()
# #     except:
# #         pass  # No overlay present
# #
# #     # More interactions as needed...
#
#
#
# import time
# import pytest
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
#
# class Test_Pytest:
#
#     # @pytest.mark.regression
#     def test_Youtubesite(self):
#         # headless_option = webdriver.ChromeOptions()
#         # headless_option.add_argument("headless")
#         # driver = webdriver.Chrome(options=headless_option)
#         driver = webdriver.Chrome()
#         driver.get("https://www.youtube.com/")
#         time.sleep(5)
#         wait = WebDriverWait(driver, 10)
#         sign_in = driver.find_element(By.XPATH, '//*[@id="sign-in-button"]/yt-button-shape/a/yt-touch-feedback-shape/div/div[2]')
#         # sign_in = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="buttons"]/ytd-button-renderer/yt-button-shape/a/div[2]')))
#         sign_in.click()
# #
# #         # def test_Login_button(self):
# #         # time.sleep(4)
# #         # driver.find_element(By.ID, "nav-search-submit-button").click()
# #
# #         print("Page title", driver.title)
# #
# #         #
# #         # l = len(driver.find_elements(By.XPATH, "//div[@class='quickfinder-description gem-text-output']//p//a"))
# #         # #print(l)
# #         # Contact_Number_List =[]
# #         # for r in range(1, l+1):
# #         #     Contact_Number = driver.find_element(By.XPATH, "//div[@class='quickfinder-description gem-text-output']//p//a[" +str(r)+ "]").text
# #         #     #print(Contact_Number)
# #         #     Contact_Number_List.append(Contact_Number)
# #         # #print(Contact_Number_List)
# #         # mb = "+91 95790646580"
