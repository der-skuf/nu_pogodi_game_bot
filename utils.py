import cv2
from mss import mss
from numpy import array, where

from settings import monitor


def get_gray_screenshoot():
    with mss() as sct:
        img = array(sct.grab(monitor))
    gray_monitor_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return gray_monitor_img

def read_gray_img(img_path):
    image = cv2.imread(img_path, cv2.COLOR_BGR2GRAY)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return gray_image


def match_template(image, template, threshold=0.8):
    res = cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)
    loc = where(res >= threshold)
    return loc
