"""登录模块测试用例（等价类划分）。"""


def login(user: str, pwd: str) -> str:
    """被测函数：仅做格式校验，便于实验演示。"""
    if not user and not pwd:
        return "账号和密码不能为空"
    if not user:
        return "账号不能为空"
    if not pwd:
        return "密码不能为空"
    if len(pwd) < 8:
        return "密码长度不足"
    return "登录成功"


def test_valid_login():
    assert login("student01", "Passw0rd!") == "登录成功"


def test_empty_user():
    assert login("", "Passw0rd!") == "账号不能为空"


def test_empty_password():
    assert login("student01", "") == "密码不能为空"


def test_short_password():
    assert login("student01", "Pass1") == "密码长度不足"
