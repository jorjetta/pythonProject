import json
import random

from selenium import webdriver
import time
import requests
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
namelist = ['Egoryan', 'Jojoyan', 'Goharyan', 'Annayan']
name = random.choice(namelist)
last_names = ['Baklanyan', 'Mkryan', 'Dovlatyan', 'Antonyan']
lname = random.choice(last_names)
mails = ['egor.baklanyan', 'jojo_mkryan', 'goyar_bestofthebest', 'anya_anyuta']
the_mail = random.choice(mails)
try:
    driver.get("https://www.mail.ru/")
    search_input = driver.find_element(by=By.XPATH,
                                       value="//a[contains(@class, 'resplash-btn resplash-btn_outlined-blue')]").click()
    driver.switch_to.window(driver.window_handles[1])
    WebDriverWait(driver, 40).until(EC.presence_of_element_located((By.ID, "fname"))).send_keys(f"{name}")
    driver.find_element(By.ID, "lname").send_keys(f"{lname}")

    driver.find_element(By.XPATH, "//span[contains(text(), 'Day')]").click()
    driver.find_element(By.XPATH, "//span[contains(text(), '8')]").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//span[contains(text(), 'Month')]").click()
    driver.find_element(By.XPATH, "//span[contains(text(), 'Февраль')]").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//span[contains(text(), 'Year')]").click()
    driver.find_element(By.XPATH, "//span[contains(text(), '2012')]").click()

    #driver.find_element_by_css_selector("input.input-0-2-154[value='male']").click()
    #driver.find_element(by=By.CLASS_NAME, value="radio-0-2-151").click()
    driver.find_element(By.CLASS_NAME, "radio-0-2-146").click()

    driver.find_element(By.ID, value="aaa__input").send_keys(f"{the_mail}")
    driver.find_element(By.XPATH, "//span[contains(text(), '@mail.ru')]").click()
    driver.find_element(By.XPATH, "//span[contains(text(), '@bk.ru')]").click()
    time.sleep(1)
    driver.find_element(By.ID, "password").send_keys("AqSwDe12345")
    time.sleep(1)
    driver.find_element(By.CLASS_NAME, value="passwordEye-0-2-119").click()
    time.sleep(1)
    driver.find_element(By.ID, "phone-number__select").click()
    #driver.find_element(By.XPATH, "//span[contains(text(), 'United States')]").click()
    driver.find_element(By.ID, value= "phone-number__phone-input").send_keys('3672217463')

    # search_input.send_keys("Borzoi dog")
    # driver.find_element(by=By.ID, value="search_icon").click()
    #
    # WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID,
    #                                                                 "b-scopeListItem-video"))).click()
    #
    # video_items = driver.find_elements(by=By.CLASS_NAME, value="mc_vtvc_link")
    # my_urls = []
    #
    # for element in video_items:
    #     my_urls.append(element.get_attribute('href'))
    #
    #
    # print(video_items)
    # for i, url in enumerate(my_urls[:3]):
    #     # try:
    #     href = url
    #
    #     print(href)
    #
    #     driver.switch_to.default_content()
    #
    #     tab = driver.find_element(By.TAG_NAME,'body')
    #     tab.send_keys(Keys.COMMAND + 't')
    #
    #     driver.get(href)
    #
    #     frame = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.TAG_NAME,
    #                                                                     "iframe")))
    #
    #     driver.switch_to.frame(frame)
    #
    #     driver.find_element(By.CLASS_NAME, "ytp-large-play-button").click()
    #

    time.sleep(100)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()

# gtnel borzoi dog, gnal images,bacel arajin image
