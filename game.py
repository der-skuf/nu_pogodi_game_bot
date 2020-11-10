import asyncio
import webbrowser
from typing import Union

from interfaces import IGameLauncher, IGame, IPlayer
from settings import (
    game_url, imgs, all_last_egg_positions, dark_color_threshold,
    default_game_type,
)
from utils.utils import CVImage, AutoGUI


class HTMLGameLauncher(IGameLauncher):
    gui = AutoGUI
    cvimg = CVImage

    @staticmethod
    async def _open_browser(await_time: int) -> bool:
        webbrowser.open(game_url, autoraise=0)
        await asyncio.sleep(await_time)
        return True

    @classmethod
    async def has_launched(cls):
        await cls._open_browser(await_time=5)
        kwargs_match_template_and_click = [
            {
                'template_img_path': imgs.get_nested_filename('launch.full_window_btn_png'),
                'sleep_time': 6
            },
            {
                'template_img_path': imgs.get_nested_filename('launch.rus_flag_png'),
                'sleep_time': 2
            },
            {
                'template_img_path': imgs.get_nested_filename('launch.start_game_png'),
                'sleep_time': 1
            },
            {
                'template_img_path': imgs.get_nested_filename('launch.submit_instruction_btn_png'),
                'sleep_time': 1
            },
        ]

        for click_data in kwargs_match_template_and_click:
            if not await cls.cvimg.match_template_and_click(**click_data):
                err_text = f'Launcher has failed on {click_data["template_img_path"]} image'
                cls.gui.alert(text=err_text, title='launcher has failed', button='close', timeout=3 * 1000)

                return False
        return True


class PlayerBot(IPlayer):
    gui = AutoGUI

    @classmethod
    async def _detect_egg(cls, offset_value, image, position_name):
        '''
            По сути весь механизм проверки это просто сверять наличие пикселя в конкретной точке
            Как оказалось это самый простой способ нахождения яиц. Этого достаточно чтобы набить 999
        '''
        x, y = list(offset_value.values())[::-1]
        if dark_color_threshold > image[y][x]:
            return position_name

    @classmethod
    async def detect_egg(cls, image, all_last_egg_positions) -> Union[None, str]:
        results = list()
        for position_name, offset_value in all_last_egg_positions.items():
            detect_task = asyncio.create_task(cls._detect_egg(offset_value, image, position_name))
            results.append(detect_task)
        tasks = await asyncio.gather(*results)
        eggs = [x for x in tasks if x]
        return eggs[0] if len(eggs) else None

    @classmethod
    async def egg_pick_up(cls, egg_position) -> bool:
        buttons_to_click = {
            'top_right': 'e',
            'top_left': 'q',
            'bottom_right': 'd',
            'bottom_left': 'a',
        }
        return cls.gui.press(buttons_to_click[egg_position])


class Game(IGame):
    launcher = HTMLGameLauncher
    player = PlayerBot
    cvimg = CVImage

    @classmethod
    async def check_alive(cls):
        '''Бот как бы в принципе не проигрывает, поэтому оказалось ненужным'''
        return True
        pass

    @classmethod
    async def restart(cls):
        pass

    @classmethod
    async def play_game(cls):
        prev_pos = None  # Чтобы не закликивать сотню раз
        try:
            while await cls.check_alive():
                image = cls.cvimg.get_gray_screenshoot()
                # if egg_position := cls.player.detect_egg(image, all_last_egg_positions):
                egg_position = await cls.player.detect_egg(image, all_last_egg_positions)
                if egg_position and (egg_position != prev_pos):
                    await cls.player.egg_pick_up(egg_position)
                    prev_pos = egg_position
            cls.restart()
        except KeyboardInterrupt:
            print('The game has stopped working by KeyboardInterrupt')
            pass

    @classmethod
    async def _click_start_game(cls, path=default_game_type) -> bool:
        result = await cls.cvimg.match_template_and_click(template_img_path=path, sleep_time=1)
        return result

    @classmethod
    async def start(cls):
        if await cls.launcher.has_launched():
            is_click = await cls._click_start_game()
            await cls.play_game()
        pass
