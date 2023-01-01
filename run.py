import os
import time

import pytest
from commom.yaml_util import write_yaml, read_yaml, clear_yaml

if __name__ == '__main__':
    pytest.main()
    time.sleep(3)
    os.system("allure generate ./temps -o ./reports --clean")
