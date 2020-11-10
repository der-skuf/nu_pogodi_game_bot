import asyncio
import cv2
import pyautogui
from mss import mss
from numpy import array as nparray, where, mean, ndarray
from typing import Tuple

from interfaces import CV2Interface, CVImageInterface, IAutoGUI
from settings import monitor, default_threshold


class CV2Engine(CV2Interface):
    @staticmethod
    def cvtColor(img, color=cv2.COLOR_BGR2GRAY):
        return cv2.cvtColor(img, color)

    @staticmethod
    def matchTemplate(image, template, method=cv2.TM_CCOEFF_NORMED, **kwargs):
        return cv2.matchTemplate(image, template, method, **kwargs)

    @staticmethod
    def imread(img_path, color=cv2.COLOR_BGR2GRAY):
        return cv2.imread(img_path, color)

    @staticmethod
    def imshow(image_name, image):
        return cv2.imshow(image_name, image)

    @staticmethod
    def waitKey(key=0):
        return cv2.waitKey(key)

    @staticmethod
    def destroyAllWindows():
        return cv2.destroyAllWindows()


class AutoGUI(IAutoGUI):
    @staticmethod
    async def mouse_click(coord_x: int, coord_y: int) -> bool:
        pyautogui.click(x=coord_x, y=coord_y)
        return True

    @staticmethod
    def get_screenshoot(monitor=monitor):
        with mss() as sct:
            img = nparray(sct.grab(monitor))
        return img

    @staticmethod
    def press(key, **kwargs):
        print(f'im pressing {key}')
        pyautogui.press(key, **kwargs)
        return True

    @staticmethod
    def alert(text: str, title: str, button: str, **kwargs):
        pyautogui.alert(text=text, title=title, button=button, **kwargs)
        return True


class CVImage(CVImageInterface):
    '''Класс для работы с изображениями'''
    cv2 = CV2Engine
    gui = AutoGUI

    @classmethod
    def get_gray_screenshoot(cls, monitor=monitor):
        img = cls.gui.get_screenshoot(monitor)
        gray_monitor_img = cls.cv2.cvtColor(img)
        return gray_monitor_img

    @classmethod
    def read_gray_img(cls, img_path: str):
        image = cls.cv2.imread(img_path)
        gray_image = cls.cv2.cvtColor(image)
        return gray_image

    @classmethod
    def match_template(cls, image, template, threshold=default_threshold, **kwargs):
        res = cls.cv2.matchTemplate(image, template, **kwargs)
        loc = where(res >= threshold)
        return loc

    @staticmethod
    def get_img_center_from_loc(loc: ndarray, template_shape: Tuple[int, int]) -> Tuple:
        w, h = template_shape  # Метод вызываемый у ndarray
        center_list = list()
        for x1, y1 in zip(*loc[::-1]):
            x2, y2 = (x1 + w, y1 + h)
            center = ((x1 + x2) / 2, (y1 + y2) / 2)
            center_list.append(center)

        avg_center = tuple(map(mean, zip(*center_list)))
        return avg_center

    @classmethod
    def print_image(cls, image, image_name="Image"):
        cls.cv2.imshow(image_name, image)
        cls.cv2.waitKey(0)
        cls.cv2.destroyAllWindows()

    @staticmethod
    def locate_center_in_match_template(
            monitor_img: ndarray,
            full_src_btn_img: ndarray,
            threshold=default_threshold
    ) -> Tuple[int, int]:
        loc = CVImage.match_template(monitor_img, full_src_btn_img, threshold)
        center_img = CVImage.get_img_center_from_loc(loc, full_src_btn_img.shape[::-1])
        return center_img

    @classmethod
    async def match_template_and_click(
            cls,
            template_img_path: str,
            sleep_time: int,
            threshold=default_threshold,
            gray_monitor_img=None
    ) -> bool:
        '''Получение скриншота, поиск элемента на скрине и клик по элементу'''
        if gray_monitor_img is None:
            gray_monitor_img = CVImage.get_gray_screenshoot()

        template_img = CVImage.read_gray_img(template_img_path)
        coords = cls.locate_center_in_match_template(gray_monitor_img, template_img, threshold)

        if coords:
            await cls.gui.mouse_click(*coords)
            await asyncio.sleep(sleep_time)
            return True

        return False


def convert_monitor_to_xy(monitor):
    x1 = monitor['left']
    y1 = monitor['top']
    x2 = monitor['left'] + monitor['width']
    y2 = monitor['top'] + monitor['height']
    return (x1, y1), (x2, y2)
