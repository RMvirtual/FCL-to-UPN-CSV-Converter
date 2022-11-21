from abc import ABC, abstractmethod


class Dimensions(ABC):
    @property
    @abstractmethod
    def length(self) -> float:
        ...

    @length.setter
    @abstractmethod
    def length(self, new_length: float) -> None:
        ...

    @property
    @abstractmethod
    def width(self) -> float:
        ...

    @width.setter
    @abstractmethod
    def width(self, new_width: float) -> None:
        ...

    @property
    @abstractmethod
    def height(self) -> float:
        ...

    @height.setter
    @abstractmethod
    def height(self, new_height: float) -> None:
        ...
