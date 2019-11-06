from Common.config import init_driver
import time
import pytest


class Test_Class:

    def test_one(self):
        x = "this"
        assert "h" in x, '成功了'

    def test_two(self):
        x = "hello"
        assert x == "hi", '成功了'

# if __name__ == "__main__":
#     pytest.main(['--html=./Report/report.html','test_abc.py'])
