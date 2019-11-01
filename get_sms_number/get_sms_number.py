# 获取短信发送总量
# by hyn
# 20191101

from selenium import webdriver
import time
from PIL import Image
import requests
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'c://Program Files (x86)//Tesseract-OCR//tesseract.exe'

tessdata_dir_config = '--tessdata-dir "c://Program Files (x86)//Tesseract-OCR//tessdata"'

yzdsj_url = 'http://211.138.17.200:7097/cmsd-store-web/open/login2'
detail_url = 'http://211.138.17.200:7097/cmsd-store-web/index/productApp/detail/63'
user_name = '371SYSU'
password = '2wsx3edc1'
img_path = '123.png'
path = 'D:/download/123.jpeg'


# 登陆豫知大数据
def login():
    driver = webdriver.Chrome()
    driver.get(yzdsj_url)

    time.sleep(4)

    driver.find_element_by_name("userId").send_keys(user_name)
    driver.find_element_by_name("pwd").send_keys(password)

    image_xpath = '//*[@id="checkcodeImg"]'

    element = driver.find_element_by_xpath(image_xpath).screenshot_as_png

    i = open(path, 'wb')
    i.write(element)
    i.close()

    ocr_image()

    # picture = Image.open('123.png')
    # picture = picture.crop((xPiont, yPiont, element_width, element_height))
    # picture.save("123.png")


# 识别验证码
def ocr_image():
    im = Image.open(path)
    # threshold = 140
    # table = []
    # for i in range(256):
    #     if i < threshold:
    #         table.append(0)
    #     else:
    #         table.append(1)
    #
    # out = im.point(table, '1')
    num = pytesseract.image_to_string(im, lang='eng', config=tessdata_dir_config)

    print(num)
    return num


# 跳转到短信页面


# class GetSmsNumber():
#
#     # 初始化
#     def __init__ (self):
#         pass
#
#     def

login()
