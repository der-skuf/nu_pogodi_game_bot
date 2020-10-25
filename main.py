# from settings import game_url, monitor, full_window_btn_png, rus_flag_png
from settings import game_url, imgs
import asyncio
from numpy import ndarray, array, mean
import webbrowser
from mss import mss
import cv2
import pyautogui

from utils import match_template, read_gray_img, get_gray_screenshoot


async def open_browser():
    webbrowser.open(game_url, autoraise=0)
    await asyncio.sleep(5)
    return True
    # with mss() as sct:
    #     img = array(sct.grab(monitor))
    # return img

async def locate_center_in_match_template(monitor_img, full_src_btn_img):
    loc = match_template(monitor_img, full_src_btn_img)

    def get_img_center(xy1: ndarray, xy2: ndarray) -> tuple:
        x1, y1 = xy1
        x2, y2 = xy2
        center = ((x1 + x2) / 2, (y1 + y2) / 2)
        return center

    def get_img_center_from_loc(loc, template_shape):
        w, h = template_shape
        center_list = list()
        for pt in zip(*loc[::-1]):
            center = get_img_center(pt, (pt[0] + w, pt[1] + h))
            center_list.append(center)

        avg_center = tuple(map(mean, zip(*center_list)))
        return avg_center

    center_img = get_img_center_from_loc(loc, full_src_btn_img.shape[::-1])
    return center_img


async def mouse_click(full_src_btn_coords):
    pyautogui.click(*full_src_btn_coords)
    return True


async def main():
    await open_browser()
    gray_monitor_img = get_gray_screenshoot()
    full_src_btn_img = read_gray_img(imgs['full_window_btn_png'])
    coords = await locate_center_in_match_template(gray_monitor_img, full_src_btn_img)
    await mouse_click(coords)
    await asyncio.sleep(10)

    gray_monitor_img = get_gray_screenshoot()
    rus_flag_choose = read_gray_img(imgs['rus_flag_png'])
    rus_flag_coords = await locate_center_in_match_template(gray_monitor_img, rus_flag_choose)
    await mouse_click(rus_flag_coords)
        # print(coords)
    # await click_full_scr_btn(coords)

    print('hello world')


if __name__ == '__main__':
    asyncio.run(main())
