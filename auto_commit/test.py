from selenium import webdriver
import traceback, json

import requests, time

url = 'https://www.southwest.com/air/booking/select.html?adultPassengersCount=1&departureDate=2019-06-27&departureTimeOfDay=ALL_DAY&destinationAirportCode=ATL&fareType=USD&int=HOMEQBOMAIR&originationAirportCode=MDW&passengerType=ADULT&reset=true&returnDate=&returnTimeOfDay=ALL_DAY&seniorPassengersCount=0&tripType=oneway'
url_test = 'https://www.baidu.com'

url='http://dmp.asiainfo.com/linkus-om/hi/forward.action?page=page/health/healthImport'

driver = webdriver.Chrome()
user_name='caomi'
pass_word='3edc$RFV'
user_name_xpath='//*[@id="loginForm"]/div[1]/input'
pass_word_xpath='//*[@id="loginForm"]/div[2]/input'
login_xpath='//*[@id="loginBtn"]'

#url='https://www.baidu.com/'
driver.get(url)

driver.find_element_by_xpath(user_name_xpath).send_keys(user_name)
driver.find_element_by_xpath(pass_word_xpath).send_keys(pass_word)
driver.find_element_by_xpath(login_xpath).click()




