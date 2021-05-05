from PIL import Image
from pytesseract import *
import re
import cv2
# from namu_main import work_share


def getQty(stock_name):
    my_shares_list = {"SOXL": 5, "DFEN": 2, "TPOR": 2, "FNGU": 9,
                      "WEBL": 6, "NAIL": 3, "QLD": 4, "TQAQQ": 4, "TQQQ": 4, "BNKD": 20}
    stock_qty = my_shares_list[stock_name]
    return stock_qty


def pyt_stock_name():
    file_name = "file/stock_name.txt"
    img = Image.open("img/var/stock_name.png")
    text = pytesseract.image_to_string(img)
    with open(file_name, "w")as f:
        f.write(text)
    with open(file_name, "r")as file:
        stock_name = file.readlines()
    stock_name = stock_name[0].replace("\n", "").replace(".", "")
    my_shares_list = ["DFEN", "TPOR", "SOXL",
                      "WEBL", "NAIL", "QLD", "TQAQQ", "TQQQ", "FNGU", "BNKD"]
   # print(my_shares_list)
    if stock_name in my_shares_list:
        print(f"{stock_name} : 무한매수를 진행합니다.")
        stock_price(stock_name)
        return stock_name
    else:
        print(f"{stock_name} : 무한매수를 진행할 종목이 아닙니다.")
        stock_name = "nono"
        return stock_name


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
    # stock_name = stock_name[0].replace("\n", "")
    # file_name = f"file/{stock_name}_price.txt"
    file_name = f"file/{stock_name}_price.txt"
    img = Image.open("img/var/stock_info.png")
    text = pytesseract.image_to_string(img, config=config)
    f = open(f"file/{stock_name}_price.txt", 'w')
    f.close()
    with open(file_name, "w")as f:
        f.write(text)
    with open(file_name, "r")as file:
        # stock_price = file.readlines()
        price_replace(file_name)
    return print(f"{stock_name} : 변환완료")


# pyt_stock_name()
# pyt(today_stock_img, today_stock_file)
