import cv2
import pytest

from settings import imgs


@pytest.fixture
def full_window_btn():
    test = cv2.imread(imgs['full_window_btn_png'], cv2.COLOR_BGR2GRAY)
    return cv2.cvtColor(test, cv2.COLOR_BGR2GRAY)


@pytest.fixture
async def full_src_btn_coords():
    return (747.0, 912.6666666666666)


@pytest.fixture
async def full_window_btn_png():
    return imgs['full_window_btn_png']


@pytest.fixture
async def opened_game_screenshoot():
    opened_game_screenshoot = cv2.imread(imgs['opened_game_screenshoot_png'], cv2.COLOR_BGR2GRAY)
    gray_frame = cv2.cvtColor(opened_game_screenshoot, cv2.COLOR_BGR2GRAY)
    return gray_frame
