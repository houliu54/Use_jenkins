# 输出一个测试报告
import pytest,allure_pytest



class TestBug(object):
    @pytest.mark.parametrize('name', ['bug'])
    def testcase1(self,name):
        assert name =="bug"

if __name__ == "__main__":
    pytest.main(['-vs'])