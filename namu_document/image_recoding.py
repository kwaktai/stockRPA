from PIL.ImageOps import grayscale
import pyautogui as pya
import mouseinfo

stock_menu = pya.locateOnScreen(
    "img/app_icon.png", grayscale=True, confidence=0.8, region=(9, 794, 100, 200))
# stock_manu_center = pya.center(stock_manu)
# pya.moveTo(stock_manu_center)
# x_p, y_p = pya.position()
# x, y = x_p/2, y_p/2
# pya.moveTo(x=x, y=y)

print(stock_menu)
