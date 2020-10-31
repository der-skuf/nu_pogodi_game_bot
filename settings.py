game_url = 'https://ollgames.ru/nu-pogodi/'
monitors = {
    '1920x1080': {"top": 0, "left": 0, "width": 1920, "height": 1080},
    '1600x900': {"top": 0, "left": 0, "width": 1600, "height": 900},
    '1440x900': {"top": 0, "left": 0, "width": 1440, "height": 900},
    '1366x768': {"top": 0, "left": 0, "width": 1366, "height": 768},
}

monitor = monitors['1920x1080']

game_screen_size = {"top": 210, "left": 500, "width": 910, "height": 650}

imgs = {
    'rus_flag_png': "imgs/rus_flag.png",
    'full_window_btn_png': "imgs/full_window_btn.png",
    'opened_game_screenshoot_png': "imgs/opened_game_screenshoot.png",
    'start_game_png': "imgs/start_game.png",
    'submit_instruction_btn_png': "imgs/submit_instruction_btn.png",
    'top_right_png': "imgs/top_right.png",
    'top_left_png': "imgs/top_left.png",
    'bottom_left_png': "imgs/bottom_left.png",
    'bottom_right_png': "imgs/bottom_right.png",
    'full_game_1920x1080_png': "imgs/full_game_1920x1080.png",
}


def get_egg_position():
    '''
        Функция высчитывает координаты каждого куриного лотка,
        откуда идут яйца относительно экрана монитора и игры.
    '''

    def get_all_chicken_egg_gutter(width=game_screen_size['width'], height=game_screen_size['height']):
        q_btn = (height / 3.42105263, width / 13)
        a_btn = (height / 1.91176471, width / 13)

        e_btn = (height / 3.42105263, width / 1.421875)
        d_btn = (height / 1.91176471, width / 1.421875)
        data = {
            'top_left': q_btn,
            'bottom_left': a_btn,
            'bottom_right': d_btn,
            'top_right': e_btn,
        }
        return data

    def get_size(top, left):
        width_game_coeff = 4.5
        height_game_coeff = 4
        game_screen_width = game_screen_size['width']
        game_screen_height = game_screen_size['height']
        data = {
            "top": top,
            "left": left,
            "width": game_screen_width / width_game_coeff,
            "height": game_screen_height / height_game_coeff
        }
        return data

    egg_position = dict()
    for position_name, coords in get_all_chicken_egg_gutter().items():
        data = {k: int(v) for k, v in get_size(*coords).items()}
        data['left'] = data['left'] + game_screen_size['left']  # Смещение экрана монитора относительно экрана игры
        data['top'] = data['top'] + game_screen_size['top']  # Смещение экрана монитора относительно экрана игры
        egg_position[position_name] = data

    return egg_position


default_threshold = 0.8

all_egg_positions = get_egg_position()
