from PIL import Image
from pytesseract import *
import re
import cv2

today_stock_img = 'test4.png'
today_stock_flie = 'today_stock_flie.txt'


def pyt(today_stock_img, today_stock_flie):
    img = Image.open("pytesseract_test/"+today_stock_img)
    text = pytesseract.image_to_string(img, config='--psm 6')

    with open("pytesseract_test/"+today_stock_flie, "w")as f:
        f.write(text)
    with open("pytesseract_test/"+today_stock_flie, "r")as file:
        b = file.readlines()
    # b = f.readlines()
    print(b)


print(text)


# pyt(today_stock_img, today_stock_flie)
