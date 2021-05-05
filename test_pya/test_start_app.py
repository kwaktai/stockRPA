from PIL.ImageOps import grayscale
import pyautogui as pya
from xyp import *
import time

pya.PAUSE = 1

num = 0
while num <= 3:
    # xyp2("pass/namu_ghdie", "click", "False", 0.9)
    # xyp2("pass/namu_del", "click", "False", 0.9)
    xyp2("namu_overseas_stock_icon", "click", "False", 0.9)

    print(f"성공 : {num}")
    num = num + 1
