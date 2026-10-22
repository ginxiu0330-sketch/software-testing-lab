"""hello.py 的单元测试（由学生B补充）。"""

import hello


def test_greet():
    assert "World" in hello.greet("World")


def test_add():
    assert hello.add(1, 2) == 3
    assert hello.add(-1, 1) == 0


def test_multiply():
    assert hello.multiply(3, 4) == 12
    assert hello.multiply(0, 5) == 0
