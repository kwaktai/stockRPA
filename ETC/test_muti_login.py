from PIL.ImageOps import grayscale
import pyautogui as pya
from xyp import *
import time
from PIL import Image
from pytesseract import *
import FinanceDataReader as fdr
import pyt_kana as pyt


def namu_pass_longin():
    if xyp_last("namu_login_icon", "click", "False", 0.85):
        print("로그인시도")
    else:
        xyp_last("namu_login_icon", "click", "False", 0.85)
        print("오전 로그인시도")
    # time.sleep(5)
    for i in reversed(range(1, 2)):
        print(f"대기 : {i}")
        i = i + 1
        time.sleep(1)
