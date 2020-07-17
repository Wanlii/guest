
import sys
import unittest

from ddt import ddt, data, file_data, unpack
from os.path import dirname, abspath
import xmlrunner

BASE_DIR = dirname(dirname(abspath(__file__)))
BASE_DIR.replace("\\", "/")
sys.path.append(BASE_DIR)
print(BASE_DIR)
print(BASE_DIR + '/api/case_data.json')


@ddt
class TestSuit(unittest.TestCase):
    datas = []

    @unpack
    @file_data(BASE_DIR + '/api/case_data.json')
    # @data(*datas)
    def test_dicts(self, name, interface, parameter, before_Sql, after_Sql, check, rely, extract, env):
        print(name, interface, parameter, before_Sql, after_Sql, check, rely, extract, env)


# 运行测试用例
def run_case():
    with open('./result.xml', 'w+') as out:
        unittest.main(
            testRunner=xmlrunner.XMLTestRunner(out), failfast=False, buffer=False, catchbreak=False
        )


# 重写TestResult的addSuccess方法
# def addSuccess()
if __name__ == '__main__':
    run_case()