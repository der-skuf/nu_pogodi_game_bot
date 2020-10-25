import pytest
import cv2
# from settings import full_window_btn_png, opened_game_screenshoot_png
from settings import imgs

from main import open_browser


@pytest.fixture
def full_window_btn():
    return cv2.imread(imgs['full_window_btn_png'], cv2.COLOR_BGR2GRAY)


@pytest.fixture
async def full_src_btn_coords():
    return 749.0, 909.9428571428572


@pytest.fixture
async def opened_game_screenshoot():
    opened_game_screenshoot = cv2.imread(imgs['opened_game_screenshoot_png'], cv2.COLOR_BGR2GRAY)
    gray_frame = cv2.cvtColor(opened_game_screenshoot, cv2.COLOR_BGR2GRAY)
    return gray_frame
