import pytest

from main import open_browser, locate_center_in_match_template, mouse_click

from utils import match_template
# color_yellow = (0, 255, 255)

@pytest.mark.asyncio
async def test_has_game(opened_game_screenshoot, full_window_btn):
    loc = match_template(opened_game_screenshoot, full_window_btn)
    assert any([len(x) for x in loc])

@pytest.mark.asyncio
async def test_locate_full_scr_btn(opened_game_screenshoot, full_window_btn, full_src_btn_coords):
    btn_location = await locate_center_in_match_template(opened_game_screenshoot, full_window_btn)
    assert all([int(x) for x in btn_location])
    assert btn_location == full_src_btn_coords

@pytest.mark.asyncio
async def test_click_full_scr_btn(full_src_btn_coords):
    clicked = await mouse_click(full_src_btn_coords)
    assert clicked

    # x_axis
    # y_axis
    # import ipdb; ipdb.set_trace()


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

