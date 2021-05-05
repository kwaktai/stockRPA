from PIL.ImageOps import grayscale
import pyautogui as pya
from xyp import *
from PIL import Image
from pytesseract import *
from pyt import *


a = "aaa"


def certLogin():
    xyp_last("app_icon", "click", "True", 0.8)
    xyp_last("n_loginButon", "click", "True", 0.8)
    xyp_last("n_selectLogin", "click", "True", 0.8)
    xyp_last("n_selectCertification", "click", "True", 0.8)
    xyp_last("n_certification", "click", "True", 0.8)
    xyp_last("n_"+"r", "click", "True", 0.8)
    xyp_last("n_"+"h", "click", "True", 0.9)
    xyp_last("n_"+"k", "click", "True", 0.9)
    xyp_last("n_"+"r", "click", "True", 0.9)
    xyp_last("n_"+"5", "click", "True", 0.8)
    xyp_last("n_"+"2", "click", "True", 0.8)
    xyp_last("n_"+"4", "click", "True", 0.8)
    xyp_last("n_"+"1", "click", "True", 0.8)
    xyp_last("n_"+"sign", "click", "True", 0.8)
    xyp_last("n_"+"^", "click", "True", 0.8)
    xyp_last("n_"+"^", "click", "True", 0.8)
    xyp_last("n_"+"return", "click", "True", 0.8)
    return print("로그인성공")


def logout():
    xyp_last("n_"+"allMenu", "click", "True", 0.95)
    xyp_last("n_"+"logout", "click", "True", 0.95)
    xyp_last("n_"+"logout_check", "click", "True", 0.95)


def UserChange():
    # xyp_last("n_"+"certification_bar", "click", "True", 0.9)

    xyp_last("n_"+"CheckNameKWAK", "click", "True", 0.95)

    # xyp_last("n_"+"n_NameLee", "click", "True", 0.9)


def checkUser():
    target = find_target("n_CheckNameKWAK")
    print(target)
    # xyp_last("n_"+"CheckNameKWAK", "click", "True", 0.95)


def findUser():
    xyp2("namu_app_name", "click", "False", 0.95)
    x, y = pya.position()
    pya.screenshot('img/checkUser.png',
                   region=((x*2)-250, (y)+470, 140, 60))
    img = Image.open("img/checkUser.png")
    text = pytesseract.image_to_string(img, lang='kor', config="--psm 6")
    userNmae = f"{text[0]}{text[1]}{text[2]}"
    userList = ["곽일태", "이가은"]
    return userNmae
