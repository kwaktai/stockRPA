from PIL.ImageOps import grayscale
import pyautogui as pya
from xyp import xyp
import time

pya.PAUSE = 1


namu_app_icon = pya.locateOnScreen(
    "img/namu_1.png", grayscale=True, confidence=0.9)
xyp(namu_app_icon, "click")
namu_app_icon = pya.locateOnScreen(
    "img/namu_1.png", grayscale=True, confidence=0.9)
xyp(namu_app_icon, "click")
namu_app_icon = pya.locateOnScreen(
    "img/namu_4.png", grayscale=True, confidence=0.9)
xyp(namu_app_icon, "click")
namu_app_icon = pya.locateOnScreen(
    "img/namu_5.png", grayscale=True, confidence=0.9)
xyp(namu_app_icon, "click")
namu_app_icon = pya.locateOnScreen(
    "img/namu_0.png", grayscale=True, confidence=0.9)
xyp(namu_app_icon, "click")
namu_app_icon = pya.locateOnScreen(
    "img/namu_8.png", grayscale=True, confidence=0.9)
xyp(namu_app_icon, "click")
