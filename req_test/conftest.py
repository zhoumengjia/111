# 专门用来保存固件
import pytest
from commom.yaml_util import clear_yaml


@pytest.fixture(scope="session", autouse=True)
def my_fixture():
    print("\nfixture:这是前置的方法")
    # 执行之前进行清空
    clear_yaml()
    yield
    # 执行之后进行清空
    # clear_yaml()
    print("\nfixture:这是后置的方法")