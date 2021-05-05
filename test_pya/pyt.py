from PIL import Image
from pytesseract import *
import re
import cv2


def pyt_stock_name():
    file_name = "file/stock_name.txt"
    img = Image.open("img/var/stock_name.png")
    text = pytesseract.image_to_string(img)
    with open(file_name, "w")as f:
        f.write(text)
    with open(file_name, "r")as file:
        stock_name = file.readlines()
    stock_price(stock_name)
    return stock_name[0].replace("\n", "")


def price_replace(text):
    with open(text, "r")as file:
        price_list = file.readlines()
        file.close()
    a_1 = price_list[0].replace(" ", "\n")
    a_2 = price_list[1].replace(" ", "\n")
    a_list = a_1+a_2
    with open(text, "w")as file:
        file.write(a_list)
        file.close()


def stock_price(stock_name, config='--psm 6'):
    stock_name = stock_name[0].replace("\n", "")
    file_name = f"file/{stock_name}_price.txt"
    img = Image.open("img/var/stock_info.png")
    text = pytesseract.image_to_string(img, config=config)
    with open(file_name, "w")as f:
        f.write(text)
    with open(file_name, "r")as file:
        # stock_price = file.readlines()
        price_replace(file_name)
    return print(f"{stock_name} : 변환완료")


# pyt_stock_name()
# pyt(today_stock_img, today_stock_file)
