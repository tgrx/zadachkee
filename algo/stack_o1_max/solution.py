import abc
from typing import Generic
from typing import Protocol
from typing import TypeVar


class Comparable(Protocol):
    @abc.abstractmethod
    def __ge__(self: "T", other: "T") -> bool:
        pass


T = TypeVar("T", bound=Comparable)


class Stack(Generic[T]):
    def __init__(self) -> None:
        self._elements: list[T] = []
        self._max: None | T = None
        self._max_history: list[T] = []

    def push(self, element: T) -> "Stack":
        self._elements.append(element)

        if self._max is None or element >= self._max:
            self._max = element
            self._max_history.append(self._max)

        return self

    def pop(self) -> T:
        element = self._elements.pop()

        if element == self._max:
            self._max_history.pop()
            self._max = self._max_history[-1] if self._max_history else None

        return element

    @property
    def maximum(self) -> None | T:
        return self._max
