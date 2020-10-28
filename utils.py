import cv2
import pyautogui
from mss import mss
from numpy import array as nparray, where, mean, ndarray
from typing import Tuple

from interfaces import CV2Interface, CVImageInterface
from settings import monitor


class CV2Engine(CV2Interface):
    @staticmethod
    def cvtColor(img, color=cv2.COLOR_BGR2GRAY):
        return cv2.cvtColor(img, color)

    @staticmethod
    def matchTemplate(image, template, method=cv2.TM_CCOEFF_NORMED):
        return cv2.matchTemplate(image, template, method)

    @staticmethod
    def imread(img_path, color=cv2.COLOR_BGR2GRAY):
        return cv2.imread(img_path, color)


class CVImage(CVImageInterface):
    '''Класс для работы с изображениями'''
    cv2 = CV2Engine

    @classmethod
    def get_gray_screenshoot(cls):
        with mss() as sct:
            img = nparray(sct.grab(monitor))
        gray_monitor_img = cls.cv2.cvtColor(img)
        return gray_monitor_img

    @classmethod
    def read_gray_img(cls, img_path: str):
        image = cls.cv2.imread(img_path)
        gray_image = cls.cv2.cvtColor(image)
        return gray_image

    @classmethod
    def match_template(cls, image, template, threshold=0.8):
        res = cls.cv2.matchTemplate(image, template)
        loc = where(res >= threshold)
        return loc

    @staticmethod
    def get_img_center_from_loc(loc: ndarray , template_shape: Tuple[int, int]) -> Tuple:
        w, h = template_shape  # Метод вызываемый у ndarray
        center_list = list()
        for x1, y1 in zip(*loc[::-1]):
            x2, y2 = (x1 + w, y1 + h)
            center = ((x1 + x2) / 2, (y1 + y2) / 2)
            center_list.append(center)

        avg_center = tuple(map(mean, zip(*center_list)))
        return avg_center


async def mouse_click(coord_x: int, coord_y: int) -> bool:
    pyautogui.click(x=coord_x, y=coord_y)
    return True
