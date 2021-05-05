from PIL.ImageOps import grayscale
import pyautogui as pya
from xyp import *
import time
from PIL import Image
from pytesseract import *
import FinanceDataReader as fdr
# from pyt import *
from namu_def import namu_buy


def app_icon_click():
    xyp_last("namu_app_name", "click", "True", 0.8)


def sell_img_drag():
    xyp_last("drag_img1", "move", "False", 0.95)
    pya.drag(0, -50, 0.5, button="left")


def sell_img_scroll(i):
    xyp_last("drag_img1", "move", "False", 0.95)
    pya.scroll(-7+(-i*7))


def find_share_name(y_point):
    xyp2("namu_app_name", "click", "False", 0.95)
    sell_img_drag()
    pya.move(0, 50)
    # pya.scroll(70)
    xyp2("avg_img", "move", "False", 0.95)
    pya.move(0, 469)
    # pya.hscroll(-70)
    # sell_img_scroll()
    # xyp2("namu_app_name", "click", "False", 0.95)
    xyp2("share_lists", "move", "False", 0.95)
    pya.move(80, y_point)
    x, y = pya.position()
    pya.screenshot('img/var/stock_name.png',
                   region=((x*2)-100, (y*2)-30, 150, 50))
    pya.screenshot('img/var/stock_info.png',
                   region=((x*2)+150, (y*2)-100, 500, 120))
    return x, y


def start_buy(x=10):

    for i in range(4, x):
        if i < 5:
            print(f"현재 좌표는 : {i}")
            find_share_name(78+(i*60))
            xyp_last(f"back_icon", "click", "False", 0.95)
            xyp_last(f"namu_overseas_stock_icon", "click", "False", 0.95)

        else:
            print(f"현재 좌표는 : {i} (5이상)")
            sell_img_scroll(i-5)
            find_share_name(78+(4*60))
            xyp_last(f"back_icon", "click", "False", 0.95)
            xyp_last(f"namu_overseas_stock_icon", "click", "False", 0.95)


start_buy()
