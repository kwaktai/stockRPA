from PIL.ImageOps import grayscale
import pyautogui as pya
from xyp import *
import time
from pyt import *

# xyp2("namu_app_name", "click", "False", 0.95)
# pya.move(0, 572-103)
# pya.hscroll(-70)
# x, y = pya.position()
# pya.screenshot('img/var/today_stock.png', region=(x*2, y*2, 480, 120))


def find_share_name(y_point):
    xyp2("namu_app_name", "click", "False", 0.95)
    pya.move(0, 572-103)
    pya.hscroll(-70)
    # xyp2("namu_app_name", "click", "False", 0.95)
    # xyp2("share_lists", "move", "False", 0.95)
    # y_point = 74
    # pya.move(80, y_point)
    # x, y = pya.position()
    # pya.screenshot('img/var/stock_name.png',
    #                region=((x*2)-100, (y*2)-30, 150, 50))
    # pya.screenshot('img/var/stock_info.png',
    #                region=((x*2)+150, (y*2)-100, 500, 120))
    # return x, y


find_share_name(74)
