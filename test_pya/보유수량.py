from PIL.ImageOps import grayscale
import pyautogui as pya
from xyp import *
from pyt import *
import time


def find_share_name():
    xyp2("namu_app_name", "click", "False", 0.95)
    # pya.move(-110, 520)  # 1번 종목
    pya.move(-110, 580)  # 2번 종목
    x, y = pya.position()
    pya.screenshot('img/var/stock_name.png',
                   region=((x*2)-100, (y*2)-30, 150, 50))
    pya.screenshot('img/var/stock_info.png',
                   region=((x*2)+100, (y*2)-100, 500, 120))


# find_share_name()
