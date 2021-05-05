import pyautogui as pya
import time


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
        return pya.click(x=x, y=y), print(f"{pngfile} : 클릭 성공")
    elif s == "move":
        return pya.moveTo(x=x, y=y), print(f"{pngfile} : 이동 성공")
    else:
        print("??")


def find_target(img_file, g="True", c=0.8, timeout=5):
    start = time.time()
    target = None
    while target is None:
        target = pya.locateOnScreen(
            f"img/{img_file}.png", grayscale=g, confidence=c)
        # print(target)
        end = time.time()
        if end - start > timeout:
            break
    return target


def xyp_last(img_file, slt="click", g="True", c=0.8, timeout=5):
    target = find_target(img_file, g, c, timeout)
    if target:
        target_canter = pya.center(target)
        x_p, y_p = target_canter
        x, y = x_p/2, y_p/2
        s = str(slt)
        if s == "xy":
            return x, y
        elif s == "click":
            return pya.click(x=x, y=y), print(f"{img_file} : 클릭 성공")
            # print(f"{pngfile} : 처리 성공")
        elif s == "move":
            return pya.moveTo(x=x, y=y), print(f"{img_file} : 이동 성공")
        else:
            print("??")
    else:
        print(f'Error : {img_file}')


def trade_pw():
    if find_target("pw_check_off", "True", 0.8, 1):
        xyp_last(f"pw_check_off", "click", "False", 0.95)
        time.sleep(0.5)
        xyp_last("pass/pass_sfsg", "click", "False", 0.95)
        time.sleep(0.5)
        xyp_last("pass/pass_duvyh", "click", "False", 0.95)
        time.sleep(0.5)
        xyp_last("pass/pass_cyrhf", "click", "False", 0.95)
        time.sleep(0.5)
        xyp_last("pass/pass_wervhd", "click", "False", 0.95)
        time.sleep(0.5)
        xyp_last("pass/pass_check_box", "click", "False", 0.95)
        time.sleep(0.5)
        xyp_last("pass/pass_return", "click", "False", 0.95)
        return print("trade p/w off")
    elif find_target("pw_check_on", "True", 0.8, 1):
        print("trade p/w Check OK!")


def check_loc():
    if find_target("loc_check", "True", 0.8, 1):
        print("LOC 거래 Check OK!.")
        return
    elif find_target("basic_price", "True", 0.8, 1):
        xyp_last("basic_price", "click", "False", 0.95)
        xyp_last("loc_price", "click", "False", 0.95)
        print("LOC 거래로 변경 완료.")
        return


# def sell_img_scroll():
#     xyp_last("sell_img", "move", "False", 0.95)


def sell_img_drag():
    xyp_last("drag_img1", "move", "False", 0.95)
    pya.drag(0, -50, 0.5, button="left")


# def sell_img_scroll():
#     xyp2("namu_app_name", "click", "False", 0.95)
#     xyp_last("drag_img1", "move", "False", 0.95)
#     pya.scroll(-14)


sell_img_drag()

# 종목 간격은 63
