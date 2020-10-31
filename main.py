import asyncio
import pyautogui
import webbrowser
from numpy import ndarray
from typing import Tuple

from interfaces import IGameLauncher
from settings import game_url, imgs, default_threshold
from utils import CVImage, AutoGUI


class HTMLGameLauncher(IGameLauncher):
    @staticmethod
    async def _locate_center_in_match_template(
            monitor_img: ndarray,
            full_src_btn_img: ndarray,
            threshold=default_threshold
    ) -> Tuple[int, int]:
        loc = CVImage.match_template(monitor_img, full_src_btn_img, threshold)
        center_img = CVImage.get_img_center_from_loc(loc, full_src_btn_img.shape[::-1])
        return center_img

    @classmethod
    async def _match_template_and_click(
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
        coords = await cls._locate_center_in_match_template(gray_monitor_img, template_img, threshold)

        if coords:
            await AutoGUI.mouse_click(*coords)
            await asyncio.sleep(sleep_time)
            return True

        return False

    @staticmethod
    async def open_browser(await_time: int) -> bool:
        webbrowser.open(game_url, autoraise=0)
        await asyncio.sleep(await_time)
        return True

    @classmethod
    async def has_launched(cls):
        await cls.open_browser(await_time=5)
        kwargs_match_template_and_click = [
            {
                'template_img_path': imgs['full_window_btn_png'],
                'sleep_time': 6
            },
            {
                'template_img_path': imgs['rus_flag_png'],
                'sleep_time': 2
            },
            {
                'template_img_path': imgs['start_game_png'],
                'sleep_time': 1
            },
            {
                'template_img_path': imgs['submit_instruction_btn_png'],
                'sleep_time': 1
            },
        ]

        for click_data in kwargs_match_template_and_click:
            if not await cls._match_template_and_click(**click_data):
                err_text = f'Launcher has failed on {click_data["template_img_path"]} image'
                AutoGUI.alert(text=err_text, title='launcher has failed', button='close',timeout=3 * 1000)

                return False
        return True


async def main():
    game_has_ready = await HTMLGameLauncher.has_launched()
    if game_has_ready:
        print('ready to start')
    else:
        print('failed')

    return True


if __name__ == '__main__':
    asyncio.run(main())
