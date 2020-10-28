from abc import abstractstaticmethod, abstractmethod, abstractclassmethod, ABC

from typing import Tuple


class CVImageInterface(ABC):
    @abstractstaticmethod
    def get_img_center_from_loc(loc, template_shape) -> Tuple:
        pass

    @abstractclassmethod
    def get_gray_screenshoot(cls):
        pass

    @abstractclassmethod
    def read_gray_img(cls, img_path: str):
        pass

    @abstractclassmethod
    def match_template(cls, image, template, threshold):
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


class IGameLauncher(ABC):
    @abstractclassmethod
    def has_launched(cls) -> bool:
        ''' Метод должен релизовать запуск игры и довести до момента "старт" '''
        pass
