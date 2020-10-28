import pytest

from main import HTMLGameLauncher
from utils import CVImage, mouse_click


@pytest.mark.asyncio
async def test_has_game(opened_game_screenshoot, full_window_btn):
    loc = CVImage.match_template(opened_game_screenshoot, full_window_btn)
    assert any([len(x) for x in loc])


@pytest.mark.asyncio
async def test_locate_full_scr_btn(opened_game_screenshoot, full_window_btn, full_src_btn_coords):
    btn_location = await HTMLGameLauncher._locate_center_in_match_template(opened_game_screenshoot, full_window_btn)
    assert all([int(x) for x in btn_location])
    assert btn_location == full_src_btn_coords


@pytest.mark.asyncio
async def test_click_full_scr_btn(full_src_btn_coords):
    clicked = await mouse_click(*full_src_btn_coords)
    assert clicked


@pytest.mark.asyncio
async def test_match_template_and_click(opened_game_screenshoot, full_window_btn_png):
    assert await HTMLGameLauncher._match_template_and_click(full_window_btn_png, 0, opened_game_screenshoot)

    # cv2.imwrite('opened_game_screenshoot.png', opened_game_screenshoot)
    # loc.count()
    # import ipdb; ipdb.set_trace()
    # top_left = max_loc
    # bottom_right = (top_left[0] + w, top_left[1] + h)
    # cv2.rectangle(opened_game_screenshoot, top_left, bottom_right, 255, 2)
    # print()
    # cv2.imshow("Image", opened_game_screenshoot)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    # assert res
    # game = start_game()
