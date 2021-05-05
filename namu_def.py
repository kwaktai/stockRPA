from PIL.ImageOps import grayscale
import pyautogui as pya
from xyp import *
from PIL import Image
from pytesseract import *
import FinanceDataReader as fdr
import pyt as pyt
from datetime import datetime
import time
# import namu_main

# from pyt import *

pya.PAUSE = 0.3


def stand_by_time(TraketTime):
    now = datetime.now()
    nowDate = now.strftime('%Y-%m-%d')
    dt_want = nowDate + ' ' + TraketTime
    want_time = datetime.strptime(dt_want, '%Y-%m-%d %H:%M:%S')
    while datetime.now() < want_time:
        print(datetime.now().strftime('%H:%M:%S'))
        # print('stand_by')
        time.sleep(1)


def findBuyingtime():
    now = datetime.now()
    nowHour = int(now.strftime('%H'))
    nowMin = int(now.strftime('%M'))
    if 6 <= nowHour < 22:
        if nowHour == 21 and nowMin > 53:
            TraketTime = ("22:00:00")
            nowDate = now.strftime('%Y-%m-%d')
            dt_want = nowDate + ' ' + TraketTime
            want_time = datetime.strptime(dt_want, '%Y-%m-%d %H:%M:%S')
            while datetime.now() < want_time:
                print(datetime.now().strftime('%H:%M:%S'))
        # print('stand_by')
                time.sleep(1)
        return "res"
    else:
        return "basic"


def app_icon_click():
    xyp_last("app_icon", "click", "True", 0.8)

    # time.sleep(1)
    stock_folder_icon = pya.locateOnScreen(
        "img/stock_folder.png", grayscale=True, confidence=0.8)
    x = xyp(stock_folder_icon, "xy")
    pya.click(x=x[0], y=x[1]*2)

    xyp_last("namu_app_icon", "click")
    xyp_last("continue", "click", "True", 0.8)
    xyp_last("close", "click")
    # login_icon_if = xyp_last("namu_login_icon", "move", "False", 0.85)


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

    xyp_last("n_selectLogin", "click", "False", 0.9)
    xyp_last("n_simpleLogin", "click", "False", 0.9)
    xyp_last("n_simpleLogin_Click", "click", "False", 0.9)

    xyp_last("pass/namu_23436", "click", "False", 0.9)
    xyp_last("pass/namu_34546", "click", "False", 0.9)
    xyp_last("pass/namu_dkjfhg", "click", "False", 0.9)
    xyp_last("pass/namu_godkc", "click", "False", 0.99)
    xyp_last("pass/namu_12343", "click", "False", 0.99)
    xyp_last("pass/namu_ghdie", "click", "False", 0.9)
    for i in reversed(range(1, 6)):
        print(f"대기 : {i}")
        i = i + 1
        time.sleep(1)
    xyp_last("namu_overseas_stock_icon", "click", "False", 0.9)


def chg(day_p, avgc_p):
    chg = ((day_p/avgc_p)-1)*100
    return chg


def find_share_name(y_point):
    xyp2("namu_app_name", "click", "False", 0.95)
    sell_img_drag()
    pya.move(0, 50)
    # pya.scroll(70)
    xyp2("avg_img", "move", "False", 0.95)
    # pya.move(0, 469)
    pya.hscroll(-70)
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

# find_share_name(78)


# def find_share_name(y_point):
#     xyp2("namu_app_name", "click", "False", 0.95)
#     sell_img_drag()
#     pya.move(0, 50)
#     pya.scroll(70)
#     xyp2("avg_img", "move", "False", 0.95)
#     # pya.move(0, 469)
#     pya.hscroll(-70)
#     # sell_img_scroll()
#     # xyp2("namu_app_name", "click", "False", 0.95)
#     xyp2("share_lists", "move", "False", 0.95)
#     pya.move(80, y_point)
#     x, y = pya.position()
#     pya.screenshot('img/var/stock_name.png',
#                    region=((x*2)-100, (y*2)-30, 150, 50))
#     pya.screenshot('img/var/stock_info.png',
#                    region=((x*2)+150, (y*2)-100, 500, 120))
#     return x, y


def share1_name():
    xyp_last("var/stock_name", "click", "False", 0.95)
    xyp_last("buy_1", "click", "True", 0.95)
    share1_name = pyt.pyt_stock_name()  # <-- 리턴값은 None
    with open(f"file/{share1_name}_price.txt", "r")as file:
        price_lists_n = file.readlines()
        file.close()
    price_lists = []
    for i in price_lists_n:
        i_mod = i.replace("\n", "")
        price_lists.append(i_mod)
        file.close()
    if not len(price_lists) == 3:
        price_lists.pop(0)
    price_info = {
        f"{share1_name}_shares": price_lists[1], f"{share1_name}_avg_price": price_lists[0], f"{share1_name}_share_price": float(price_lists[2])*1.3, f"{share1_name}_share_sell_price": float(price_lists[0])*1.1}
    return price_info


def select_loc():
    xyp_last("basic_price", "click", "False", 0.95)
    xyp_last("loc_price", "click", "False", 0.95)


def namu_buy(t, user):
    xyp2("namu_app_name", "click", "False", 0.95)
    share_name = pyt.pyt_stock_name()
    if share_name == "nono":
        print("무한매수 대상이 아니다.")
    else:
        price_info = share1_name()
        p_info = ["_avg_price", "_share_price", "_shares"]
        select_loc()
        for f in p_info:
            if not f == "_shares":
                qty = str(pyt.getQty(share_name, user)[0])   # <--  user 수정했음
                # 주문수 변수
                buy_loc_myavg = str(
                    round(float(price_info[f"{share_name}{f}"]), 2)).replace(".", "p")
                buy_loc_myavg_p = buy_loc_myavg.replace("p", ".")
                if f == "_avg_price":
                    print(f"{share_name}: 평균단가 LOC 매매을 시작합니다.")
                    print(f"수량:{qty}")
                    print(f"단가:{buy_loc_myavg_p}")
                elif f == "_share_price":
                    print(f"{share_name}: 큰수 LOC 매매을 시작합니다.")
                    print(f"수량:{qty}")
                    print(f"단가:{buy_loc_myavg_p}")
                else:
                    print(f"{share_name}: 평균가의 10%에 매도 거래를 등록합니다.")

                # 여기에 큰수매매 / 평단매매 구분을 해준다.
                if xyp_last("qty_icon", "move", "False", 0.95):
                    xyp_last("qty_icon", "move", "False", 0.95)
                else:
                    xyp_last("pcs", "click", "False", 0.95)
                xyp_last("qty_icon", "click", "False", 0.95)
                for n in range(len(qty)):
                    p = qty[n]
                    xyp_last(f"namu_num/{p}", "click", "False", 0.95)
                # buy_qty
                xyp_last("namu_usd", "click", "False", 0.95)
                for num in range(len(buy_loc_myavg)):
                    i = buy_loc_myavg[num]
                    xyp_last(f"namu_num/{i}", "click", "False", 0.95)
                xyp_last(f"namu_num/return", "click", "False", 0.95)
                check_loc()
                trade_pw()
                # xyp_last(f"namu_num/buy_icon_basic", "click", "False", 0.9)
                xyp_last(f"namu_num/buy_icon_{t}", "click", "False", 0.95)
                xyp_last(f"namu_num/buy_send", "click", "False", 0.95)
                xyp_last(f"suss_return", "click", "False", 0.95)
            else:
                sell = str(price_info[f"{share_name}{f}"])
                sell_price = price_info[f"{share_name}_share_sell_price"]
                start_sell(sell, sell_price, t)


# def start_buy(x=5):
#     for i in range(x):
#         if not x == 5:
#             print(f"{x}번 실행")
#         else:
#             pya.scroll(-70)
#         find_share_name(78+(i*60))
#         namu_buy()
#         # xyp_last(f"now_stock_price_price", "click", "False", 0.95)
#         xyp_last(f"back_icon", "click", "False", 0.95)
#         xyp_last(f"namu_overseas_stock_icon", "click", "False", 0.95)
def sell_img_scroll_1(i):
    # xyp2("namu_app_name", "click", "False", 0.95)
    xyp_last("drag_img1", "move", "False", 0.95)
    pya.scroll(-7*(i))


def start_buy(x, t, user):
    for i in range(1, x+1):
        print(x+1)
        i = 7
        if i < 6:
            print(f"현재 좌표는 : {i}")
            find_share_name(78+((i-1)*60))
            namu_buy(t, user)
            xyp_last(f"back_icon", "click", "False", 0.95)
            xyp_last(f"namu_overseas_stock_icon", "click", "False", 0.95)

        else:
            print(f"현재 좌표는 : {i} (5이상)")
            sell_img_scroll_1(i-5)
            find_share_name(78+(4*60))
            namu_buy(t, user)
            xyp_last(f"back_icon", "click", "False", 0.95)
            xyp_last(f"namu_overseas_stock_icon", "click", "False", 0.95)


# def start_buy(x=5):
#     for i in range(x):
#         if not x == 5:
#             print(f"{x}번 실행")
#         else:
#             pya.scroll(-70)
#         find_share_name(78+(i*60))
#         namu_buy()
#         # xyp_last(f"now_stock_price_price", "click", "False", 0.95)
#         xyp_last(f"back_icon", "click", "False", 0.95)
#         xyp_last(f"namu_overseas_stock_icon", "click", "False", 0.95)


def off_namu_app():
    xyp2("namu_app_name", "click", "False", 0.95)
    pya.move(-280, 0)
    pya.click()


def start_sell(sell_qty, sell_price, t):
    # t = "res"
    # t = "basic"

    xyp_last(f"sell", "click", "False", 0.95)
    xyp_last(f"qty_icon", "click", "False", 0.95)
    sell_price_p = str(round(float(sell_price), 2))
    print("------------")
    print(f"판매수량 : {sell_qty}")
    print(f"판매가  : {sell_price_p}")

    for q in range(len(sell_qty)):
        qt = sell_qty[q]
        xyp_last(f"namu_num/{qt}", "click", "False", 0.95)
    xyp_last(f"namu_usd", "click", "False", 0.95)
    sell_price = str(round(float(sell_price), 2)).replace(".", "p")
    for p in range(len(sell_price)):
        pt = sell_price[p]
        xyp_last(f"namu_num/{pt}", "click", "False", 0.95)
    xyp_last(f"buy_check", "click", "False", 0.95)
    trade_pw()
    xyp_last(f"namu_num/sell_return_{t}", "click", "False", 0.95)
    xyp_last(f"sell_send", "click", "False", 0.95)
    xyp_last(f"sell_check", "click", "False", 0.95)


def check_holiday():
    xyp2("namu_app_name", "click", "False", 0.95)
    xyp_last(f"stock_main_icon", "click", "False", 0.95)
    xyp_last(f"stock_main_trade_icon", "click", "False", 0.95)
    if find_target("holiday_icon", "True", 0.8, 1):
        print("오늘은 휴장입니다.")
        print("프로그램을 종료합니다.")
        return quit()
    else:
        xyp_last(f"back_icon", "click", "False", 0.95)


# xyp_last(f"namu_num/return", "click", "False", 0.95)
# xyp_last(f"sell_return", "click", "False", 0.95)

# start_sell("6", "1.12121")

# start_sell()
# sell_img_drag()
# namu_app_click()
# namu_pass()
# now_stock_shares()
# trade_pass()
# namu_buy()
# time.sleep(5)

# xyp_last("namu_icon_test", "click", "False", 0.95)  # Test

# 현재 진행중인 종목을 클릭하여, 매수 매도 하는것을 구현
