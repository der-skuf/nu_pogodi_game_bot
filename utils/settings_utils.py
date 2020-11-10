import os.path

from interfaces import InterfaceImgDotDict


class ImgDotDict(dict, InterfaceImgDotDict):
    '''
        Цель класса удобно работать с вложенными путями к картинкам
        Обращаясь к ним через .
        Нап. masks.top_right.egg_1
    '''
    __getattr__ = dict.__getitem__
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__

    allowed_nested_types = (  # Разрешенные nested структуры.
        dict,
        list,
        tuple,
    )
    splitter = '.'  # Поле по которому ведется обращение к вложенности

    @staticmethod
    def img_path(data) -> str:
        '''Нужен для указаниия базовой папки картинок и расширения '''
        return f'imgs/{data}.png'

    def __getitem__(self, key):
        data = dict.__getitem__(self, key)
        return self.img_path(data)

    def _get_data_from_nested(self, path: str):
        '''Находит вложненое поле'''
        data = self
        for field in path.split(self.splitter):
            data = getattr(data, field, False)
        if not data:
            raise AttributeError(f'{self.__class__} has no attr {field}')
        return data

    def _get_file_name(self, join_path:str, filename:str) -> str:
        return f"{'/'.join(join_path)}/{filename}"

    def _is_path_exists(self, path: str) -> bool:
        return os.path.exists(path)

    def _check_allowed_nested_types(self, nested_data):
        error_msg = f'Filename type not in {self.allowed_nested_types}'
        assert isinstance(nested_data, self.allowed_nested_types), error_msg

    def get_all_nested_files(self, path) -> list:
        '''Возвращает все содержимое вложенной структуры'''
        files = list()
        nested_data = self._get_data_from_nested(path)
        self._check_allowed_nested_types(nested_data)

        for filename in nested_data.values():
            filename_path = self._get_file_name(path.split(self.splitter), filename)
            result = self.img_path(filename_path)
            if self._is_path_exists(result):
                files.append(result)
            else:
                print(f'the file {result} does not exist')
        return files

    def get_nested_filename(self, path) -> str:
        '''Возвращает конкретное содержимое вложенной структуры'''
        filename = self._get_data_from_nested(path).replace(self.splitter, '/')
        filename_path = self._get_file_name(path.split(self.splitter)[:-1], filename)
        return self.img_path(filename_path)


def get_egg_position(game_screen_size):
    '''
        Функция высчитывает координаты каждого куриного лотка,
        откуда идут яйца относительно экрана монитора и игры.
    '''

    def get_all_chicken_egg_gutter(width, height, **_):
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
    for position_name, coords in get_all_chicken_egg_gutter(**game_screen_size).items():
        data = {k: int(v) for k, v in get_size(*coords).items()}
        data['left'] = data['left'] + game_screen_size['left']  # Смещение экрана монитора относительно экрана игры
        data['top'] = data['top'] + game_screen_size['top']  # Смещение экрана монитора относительно экрана игры
        egg_position[position_name] = data

    return egg_position


def get_last_egg_positions(all_egg_positions, last_egg_offset) -> dict:
    '''Возвращает позиции последних яиц каждого из желобов'''
    result = dict()
    for egg_position, last_position_offset in last_egg_offset.items():
        result[egg_position] = dict()
        for coords_name, offset in last_position_offset.items():
            result[egg_position][coords_name] = all_egg_positions[egg_position][coords_name] + offset

    return result
