from utils.settings_utils import ImgDotDict, get_last_egg_positions, get_egg_position

game_url = 'https://ollgames.ru/nu-pogodi/'
monitor_size = '1920x1080'
monitors = {
    '1920x1080': {"top": 0, "left": 0, "width": 1920, "height": 1080},
    '1600x900': {"top": 0, "left": 0, "width": 1600, "height": 900},
    '1440x900': {"top": 0, "left": 0, "width": 1440, "height": 900},
    '1366x768': {"top": 0, "left": 0, "width": 1366, "height": 768},
}
_game_screen_size = {
    '1920x1080': {"top": 210, "left": 500, "width": 910, "height": 650},
}

monitor = monitors[monitor_size]
game_screen_size = _game_screen_size[monitor_size]

imgs = ImgDotDict({
    'game_A': 'game_A',
    'game_B': 'game_B',
    'launch': ImgDotDict({
        'rus_flag_png': "rus_flag",
        'full_window_btn_png': "full_window_btn",
        'start_game_png': "start_game",
        'submit_instruction_btn_png': "submit_instruction_btn",
    }),

    'tests': ImgDotDict({
        'opened_game_screenshoot_png': "opened_game_screenshoot",
        'full_game_1920x1080_png': "full_game_1920x1080",
        'top_right_png': "top_right",
        'top_left_png': "top_left",
        'bottom_left_png': "bottom_left",
        'bottom_right_png': "bottom_right",
        'game_case_1': ImgDotDict({
            '9': '9',
            '14': '14',
            '16': '16',
            '23': '23',
        })
    }),
})

default_threshold = 0.8

all_egg_positions = get_egg_position(game_screen_size)

last_egg_offset = {
    'bottom_right': {
        'top': 100,
        'left': 30,
    },
    'top_right': {
        'top': 130,
        'left': 30,
    },
    'bottom_left': {
        'top': 120,
        'left': 175,
    },
    'top_left': {
        'top': 140,
        'left': 170,
    }
}

all_last_egg_positions = get_last_egg_positions(all_egg_positions, last_egg_offset)

dark_color_threshold = 30
default_game_type = imgs["game_A"]
