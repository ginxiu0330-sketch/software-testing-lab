"""成绩等级判定：边界值测试用例。"""


def grade(score: int) -> str:
    """被测函数：0-100 分映射等级。"""
    if score < 0 or score > 100:
        raise ValueError("分数必须在 0-100 之间")
    if score < 60:
        return "不及格"
    if score < 85:
        return "及格"
    return "优秀"


def test_boundary_points():
    assert grade(0) == "不及格"
    assert grade(59) == "不及格"
    assert grade(60) == "及格"
    assert grade(84) == "及格"
    assert grade(85) == "优秀"
    assert grade(100) == "优秀"


def test_invalid_input():
    for bad in (-1, 101):
        try:
            grade(bad)
        except ValueError:
            continue
        raise AssertionError(f"{bad} 应当被拒绝")
