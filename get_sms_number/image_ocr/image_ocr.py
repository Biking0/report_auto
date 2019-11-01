#-*-coding:utf-8-*-

from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'c://Program Files (x86)//Tesseract-OCR//tesseract.exe'

tessdata_dir_config = '--tessdata-dir "c://Program Files (x86)//Tesseract-OCR//tessdata"'

def recognize_captcha(img_path):
    im = Image.open(img_path)
    # threshold = 140
    # table = []
    # for i in range(256):
    #     if i < threshold:
    #         table.append(0)
    #     else:
    #         table.append(1)
    #
    # out = im.point(table, '1')
    num = pytesseract.image_to_string(im,lang ='eng', config=tessdata_dir_config)

    print(num)
    return num


if __name__ == '__main__':
    #path='D:/project/github/test/image_ocr/123.jpeg'
    path='D:/download/123.jpeg'
    # path=''
    recognize_captcha(path)
    # for i in range(1, 12):
    #     img_path = str(i) + ".jpeg"
    #     res = recognize_captcha(img_path)
    #     strs = res.split("\n")
    #     if len(strs) >=1:
    #         print (strs[0])