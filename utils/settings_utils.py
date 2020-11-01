class ImgDotDict(dict):
    '''
        Цель класса удобно работать с вложенными путями к картинкам
        Обращаясь к ним через .
        Нап. masks.top_right.egg_1
    '''
    __getattr__ = dict.__getitem__
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__

    def img_path(self, data):
        '''Нужен для указаниия базовой папки картинок и расширения '''
        return f'imgs/{data}.png'

    def __getitem__(self, key):
        data = dict.__getitem__(self, key)
        return self.img_path(data)

    def _get_data_from_nested(self, path, splitter='.'):
        '''Находит вложненое поле'''
        data = self
        for field in path.split(splitter):
            data = getattr(data, field, False)
        if not data:
            raise AttributeError(f'{self.__class__} has no attr {field}')
        return data

    def get_file_name(self, join_path, filename):
        return f"{'/'.join(join_path)}/{filename}"

    def get_all_nested_files(self, path) -> list:
        '''Возвращает все содержимое вложенной структуры'''
        files = list()
        for filename in self._get_data_from_nested(path):
            filename_path = self.get_file_name(path.split('.'), filename)
            files.append(self.img_path(filename_path))
        return files

    def get_nested_filename(self, path):
        '''Возвращает конкретное содержимое вложенной структуры'''
        filename = self._get_data_from_nested(path).replace('.', '/')
        filename_path = self.get_file_name(path.split('.')[:-1], filename)
        return self.img_path(filename_path)


top_right_mask = ImgDotDict({
    '1': 'egg_top_right_mask_1',
    '2': 'egg_top_right_mask_2',
    '3': 'egg_top_right_mask_3',
    '4': 'egg_top_right_mask_4',
    '5': 'egg_top_right_mask_5',
})
top_left_mask = ImgDotDict({
    '1': 'egg_top_left_mask_1',
    '2': 'egg_top_left_mask_2',
    '3': 'egg_top_left_mask_3',
    '4': 'egg_top_left_mask_4',
    '5': 'egg_top_left_mask_5',
})
bottom_right_mask = ImgDotDict({
    '1': 'egg_bottom_right_mask_1',
    '2': 'egg_bottom_right_mask_2',
    '3': 'egg_bottom_right_mask_3',
    '4': 'egg_bottom_right_mask_4',
    '5': 'egg_bottom_right_mask_5',
})
bottom_left_mask = ImgDotDict({
    '1': 'egg_bottom_left_mask_1',
    '2': 'egg_bottom_left_mask_2',
    '3': 'egg_bottom_left_mask_3',
    '4': 'egg_bottom_left_mask_4',
    '5': 'egg_bottom_left_mask_5',
})

egg_top_right = ImgDotDict({
    '1': 'egg_top_right_mask_1',
    '2': 'egg_top_right_mask_2',
    '3': 'egg_top_right_mask_3',
    '4': 'egg_top_right_mask_4',
    '5': 'egg_top_right_mask_5'
})
egg_top_left = ImgDotDict({
    '1': 'egg_top_left_mask_1',
    '2': 'egg_top_left_mask_2',
    '3': 'egg_top_left_mask_3',
    '4': 'egg_top_left_mask_4',
    '5': 'egg_top_left_mask_5'
})
egg_bottom_right = ImgDotDict({
    '1': 'egg_bottom_right_mask_1',
    '2': 'egg_bottom_right_mask_2',
    '3': 'egg_bottom_right_mask_3',
    '4': 'egg_bottom_right_mask_4',
    '5': 'egg_bottom_right_mask_5'
})
egg_bottom_left = ImgDotDict({
    '1': 'egg_bottom_left_mask_1',
    '2': 'egg_bottom_left_mask_2',
    '3': 'egg_bottom_left_mask_3',
    '4': 'egg_bottom_left_mask_4',
    '5': 'egg_bottom_left_mask_5'
})

templates = ImgDotDict({
    'top_right': top_right_mask,
    'top_left': top_left_mask,
    'bottom_right': bottom_right_mask,
    'bottom_left': bottom_left_mask,
})
masks = ImgDotDict({
    'top_right': egg_top_right,
    'top_left': egg_top_left,
    'bottom_right': egg_bottom_right,
    'bottom_left': egg_bottom_left,
})
