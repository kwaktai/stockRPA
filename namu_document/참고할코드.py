import pyautogui as pya
import time


def find_target(img_file, timeout=30):
    start = time.time()
    target = None
    while target is None:
        target = pya.locateOnScreen(
            img_file, grayscale="False", confidence=0.9)
        print(target)
        end = time.time()
        if end - start > timeout:
            break
    return target


def my_click(img_file, timeout=30):
    target = find_target(img_file, timeout)
    if target:
        pya.moveTo(target)
    else:
        print(f'test{img_file}')
