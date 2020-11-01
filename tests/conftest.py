import pytest

from settings import imgs
from utils.utils import CVImage


@pytest.fixture
async def full_window_btn_png():
    return imgs.get_nested_filename('launch.full_window_btn_png')


@pytest.fixture
def full_window_btn(full_window_btn_png):
    return CVImage.read_gray_img(img_path=full_window_btn_png)


@pytest.fixture
async def full_src_btn_coords():
    return 747.0, 912.6666666666666


@pytest.fixture
async def opened_game_screenshoot():
    img_path = imgs.get_nested_filename('tests.opened_game_screenshoot_png')
    return CVImage.read_gray_img(img_path=img_path)


@pytest.fixture
async def full_game_1920x1080_png():
    img_path = imgs.get_nested_filename('tests.full_game_1920x1080_png')
    return CVImage.read_gray_img(img_path=img_path)


@pytest.fixture
async def all_egg_position():
    return {
        'top_left': {'top': 400, 'left': 570, 'width': 202, 'height': 162},
        'bottom_left': {'top': 549, 'left': 570, 'width': 202, 'height': 162},
        'bottom_right': {'top': 549, 'left': 1140, 'width': 202, 'height': 162},
        'top_right': {'top': 400, 'left': 1140, 'width': 202, 'height': 162}
    }
