from abc import abstractstaticmethod, abstractmethod, abstractclassmethod, ABC

from typing import Tuple


class CVImageInterface(ABC):
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


class IGameLauncher(ABC):
    @abstractclassmethod
    def has_launched(cls) -> bool:
        ''' Метод должен релизовать запуск игры и довести до момента "старт" '''
        pass


class IAutoGUI(ABC):
    @abstractstaticmethod
    async def mouse_click(coord_x: int, coord_y: int) -> bool:
        pass


    @abstractstaticmethod
    def alert(text: str, title: str, button: str, **kwargs) -> bool:
        pass
