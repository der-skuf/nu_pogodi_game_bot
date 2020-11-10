import pytest

from settings import imgs
from utils.settings_utils import ImgDotDict
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


@pytest.fixture
async def img_dot_dict_file_paths():
    return ImgDotDict({
        'launch': ImgDotDict({
            'rus_flag_png': "rus_flag",
            'full_window_btn_png': "full_window_btn",
            'start_game_png': "start_game",
            'submit_instruction_btn_png': "submit_instruction_btn",
        }),
    })


@pytest.fixture
async def all_nested_files(img_dot_dict_file_paths):
    return [f'{x}.png' for x in img_dot_dict_file_paths.launch.values()]


@pytest.fixture
async def nested_filename():
    return ImgDotDict.img_path('launch/rus_flag')


@pytest.fixture
async def egg_detect_images():
    result = list()
    for game_case_path in imgs.get_all_nested_files('tests.game_case_1'):
        result.append(CVImage.read_gray_img(game_case_path))
    return result
