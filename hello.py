#!/usr/bin/env python3
"""GitHub 协作实验用的最小代码文件：便于在 Fork + PR 环节演示"改代码 -> 提 PR"。"""


def greet(name: str) -> str:
    return f"Hello, {name}! Welcome to GitHub collaboration."


def add(a: int, b: int) -> int:
    return a + b


def multiply(a: int, b: int) -> int:
    """新增：乘法，供测试用例调用。"""
    return a * b


if __name__ == "__main__":
    print(greet("World"))
    print("1 + 2 =", add(1, 2))
