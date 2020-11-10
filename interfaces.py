from abc import abstractstaticmethod, abstractmethod, abstractclassmethod, ABC

from typing import Tuple, Union, Type


class IAutoGUI(ABC):
    @abstractstaticmethod
    async def mouse_click(coord_x: int, coord_y: int) -> bool:
        pass

    @abstractstaticmethod
    def get_screenshoot(monitor):
        pass

    @abstractstaticmethod
    def press(key: str, **kwargs) -> bool:
        pass

    @abstractstaticmethod
    def alert(text: str, title: str, button: str, **kwargs) -> bool:
        pass


class CV2Interface(ABC):
    @abstractstaticmethod
    def cvtColor(img, color):
        pass

    @abstractstaticmethod
    def matchTemplate(image, template):
        pass

    @abstractmethod
    def imread(self):
        pass

    @abstractstaticmethod
    def imshow(image_name, image):
        pass

    @abstractstaticmethod
    def waitKey(key):
        pass

    @abstractstaticmethod
    def destroyAllWindows():
        pass


class CVImageInterface(ABC):
    cv2: Type[CV2Interface]
    gui: Type[IAutoGUI]

    @abstractstaticmethod
    def get_img_center_from_loc(loc, template_shape) -> Tuple:
        pass

    @abstractclassmethod
    def get_gray_screenshoot(cls, monitor):
        pass

    @abstractclassmethod
    def read_gray_img(cls, img_path: str):
        pass

    @abstractclassmethod
    def match_template(cls, image, template, threshold):
        pass

    @abstractclassmethod
    def print_image(cls, image, image_name):
        pass


class IGameLauncher(ABC):
    gui: Type[IAutoGUI]
    cvimg: Type[CVImageInterface]

    @abstractclassmethod
    async def has_launched(cls) -> bool:
        ''' Метод должен релизовать запуск игры и довести до момента "старт" '''
        pass


class InterfaceImgDotDict(ABC):
    @abstractstaticmethod
    def img_path(data) -> str:
        pass

    @abstractmethod
    def get_all_nested_files(self, path) -> list:
        '''Возвращает все содержимое вложенной структуры'''
        pass

    @abstractmethod
    def get_nested_filename(self, path) -> list:
        '''Возвращает конкретное содержимое вложенной структуры'''
        pass


class IPlayer(ABC):
    gui: Type[IAutoGUI]

    @abstractclassmethod
    async def detect_egg(cls, image, all_last_egg_positions) -> Union[None, str]:
        pass

    async def egg_pick_up(cls, egg_position) -> bool:
        pass


class IGame(ABC):
    launcher: Type[IGameLauncher]
    player: Type[IPlayer]
    cvimg: Type[CVImageInterface]

    @abstractclassmethod
    async def restart(cls):
        pass

    @abstractclassmethod
    async def play_game(cls):
        pass

    @abstractclassmethod
    async def check_alive(cls) -> bool:
        pass

    @abstractclassmethod
    async def start(cls):
        pass
