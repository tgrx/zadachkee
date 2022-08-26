import pytest

from algo.stack_o1_max.solution import Stack


def test_empty() -> None:
    stack: Stack[int] = Stack()
    assert stack.maximum is None

    with pytest.raises(IndexError):
        stack.pop()


def test_switch() -> None:
    stack: Stack[int | str] = Stack()

    stack.push(1)
    assert stack.maximum == 1
    assert stack.pop() == 1
    assert stack.maximum is None

    stack.push("x")
    assert stack.maximum == "x"
    assert stack.pop() == "x"
    assert stack.maximum is None


def test_maximum_history() -> None:
    stack: Stack[int] = Stack()

    stack.push(4).push(4)
    assert stack.maximum == 4

    assert stack.pop() == 4
    assert stack.maximum == 4

    assert stack.pop() == 4
    assert stack.maximum is None

    stack.push(1)
    assert stack.maximum == 1

    stack.push(4)
    assert stack.maximum == 4

    stack.push(4)
    assert stack.maximum == 4

    stack.push(3)
    assert stack.maximum == 4

    stack.push(5)
    assert stack.maximum == 5

    assert stack.pop() == 5
    assert stack.maximum == 4

    assert stack.pop() == 3
    assert stack.maximum == 4

    assert stack.pop() == 4
    assert stack.maximum == 4

    assert stack.pop() == 4
    assert stack.maximum == 1

    assert stack.pop() == 1
    assert stack.maximum is None
