import pytest

from game import HTMLGameLauncher, PlayerBot
from settings import imgs, all_last_egg_positions
from utils.utils import CVImage, convert_monitor_to_xy, AutoGUI


@pytest.mark.asyncio
async def test_has_game(opened_game_screenshoot, full_window_btn):
    loc = CVImage.match_template(opened_game_screenshoot, full_window_btn)
    assert any([x.size for x in loc])


def test_locate_full_scr_btn(opened_game_screenshoot, full_window_btn, full_src_btn_coords):
    btn_location = HTMLGameLauncher.cvimg.locate_center_in_match_template(
        opened_game_screenshoot,
        full_window_btn,
        0.8
    )
    assert all([int(x) for x in btn_location])
    assert btn_location == full_src_btn_coords


@pytest.mark.asyncio
async def test_click_full_scr_btn(full_src_btn_coords):
    clicked = await AutoGUI.mouse_click(*full_src_btn_coords)
    assert clicked


@pytest.mark.asyncio
async def test_match_template_and_click(opened_game_screenshoot, full_window_btn_png):
    assert await HTMLGameLauncher.cvimg.match_template_and_click(
        template_img_path=full_window_btn_png,
        sleep_time=0,
        gray_monitor_img=opened_game_screenshoot
    )


def test_get_egg_position(all_egg_position, full_game_1920x1080_png):
    '''Тест находит позицию лотков на шаблоне игры'''
    for egg_position_name, egg_position in all_egg_position.items():
        img_path = imgs.get_nested_filename(f'tests.{egg_position_name}_png')
        egg_position_png = CVImage.read_gray_img(img_path=img_path)
        (x1, y1), (x2, y2) = convert_monitor_to_xy(egg_position)
        egg_position_from_template = full_game_1920x1080_png[y1:y2, x1:x2]
        assert HTMLGameLauncher.cvimg.locate_center_in_match_template(
            egg_position_from_template,
            egg_position_png,
            0.8
        )


@pytest.mark.asyncio
async def test_get_all_nested_files(img_dot_dict_file_paths, all_nested_files):
    all_files = img_dot_dict_file_paths.get_all_nested_files('launch')
    for filepath, filename in zip(all_files, all_nested_files):
        assert filepath.endswith(filename)


@pytest.mark.asyncio
async def test_egg_detect(egg_detect_images):
    for image in egg_detect_images:
        assert await PlayerBot.detect_egg(image, all_last_egg_positions)


@pytest.mark.asyncio
async def test_get_nested_filename(img_dot_dict_file_paths, nested_filename):
    test_nested_filename = img_dot_dict_file_paths.get_nested_filename('launch.rus_flag_png')
    assert test_nested_filename == nested_filename
