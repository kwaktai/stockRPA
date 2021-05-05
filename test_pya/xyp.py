import pyautogui as pya

# stock_menu = pya.locateOnScreen("doker.png", grayscale=True, confidence=0.8)


def xyp(pngfile, slt):
    stock_manu_center = pya.center(pngfile)
    x_p, y_p = stock_manu_center
    x, y = x_p/2, y_p/2
    s = str(slt)
    if s == "xy":
        return x, y
    elif s == "click":
        return pya.click(x=x, y=y)
    elif s == "move":
        return pya.moveTo(x=x, y=y)
    else:
        print("??")


def xyp2(pngfile, slt="click", g="True", c=0.8):
    stock_menu = pya.locateOnScreen(
        f"img/{pngfile}.png", grayscale=g, confidence=c)
    stock_manu_center = pya.center(stock_menu)
    x_p, y_p = stock_manu_center
    x, y = x_p/2, y_p/2
    s = str(slt)
    if s == "xy":
        return x, y
    elif s == "click":
        return pya.click(x=x, y=y), print(f"{pngfile} : 처리 성공")
        # print(f"{pngfile} : 처리 성공")
    elif s == "move":
        return pya.moveTo(x=x, y=y)
    else:
        print("??")


# xyp2("doker", "click", "False", 0.9)  <- Sample
# pya.moveTo(x=xyp(stock_menu)[0], y=xyp(stock_menu)[1])
