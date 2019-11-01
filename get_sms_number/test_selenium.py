from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException

import time

driver = webdriver.Chrome()
driver.get("http://211.138.17.200:7097/cmsd-store-web/open/login2")

time.sleep(4)

driver.find_element_by_name("userId").send_keys("371SYSU")
driver.find_element_by_name("pwd").send_keys("2wsx3edc1")

input_checkcode=input('input:')
driver.find_element_by_id("checkcode").send_keys(input_checkcode)

time.sleep(4)

driver.find_element_by_id("btn1").click()
time.sleep(4)

input('input:')

zx_url='http://211.138.17.200:7097/zx/index.jsp'

#input('input123:')
#driver.get(zx_url)
#input('input:')

#driver.get(zx_url)
#input('input1:')
#driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='知讯'])[1]/following::button[1]").click()
zx_xpath='//*[@id="dataProduct_con3"]/div[1]/ul/li[2]/div/button'
zx_full_xpath='/html/body/div[2]/div/div/div/div/div[1]/ul/li[2]/div/button'
zx_name_xpath='//*[@id="dataProduct_con3"]/div[1]/ul/li[2]/div/h3/a'
zx_image_xpath='//*[@id="dataProduct_con3"]/div[1]/ul/li[2]/div/a/img'
detail_url='http://211.138.17.200:7097/cmsd-store-web/index/productApp/detail/63'
#input('input2:')
#driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='知讯'])[1]/following::button[1]").click()
driver.get(detail_url)
input('input3:')

see_xpath='//*[@id="appBtn"]'
driver.find_element_by_xpath(see_xpath).click()
#driver.find_element_by_xpath(zx_xpath).click()




