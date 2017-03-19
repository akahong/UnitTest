#encoding:utf-8
import unittest

#unitest框架之testfixture结构用例
class MyTestCase(unittest.TestCase):
    def setUp(self):
        """初始化方法"""
        print "setup"

    def test_something(self):
        """测试用例方法，方法必须以test开头"""
        print "testcase"
        self.assertEqual(True, True)

    def test_anything(self):
        """测试用例方法"""
        print "testcase"
        self.assertEqual(False, False)

    def tearDown(self):
        """清除方法"""
        print "teardown"

if __name__ == '__main__':
    unittest.main()
