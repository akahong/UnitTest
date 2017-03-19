#encoding:utf-8
import TestFixture
import unittest

#1、用于控制单个测试用例的执行
mysuit=unittest.TestSuite() #声明一个testsuit对象
mysuit.addTest(TestFixture.MyTestCase("test_something")) #添加一个测试用例
mysuit.addTest(TestFixture.MyTestCase("test_anything"))

#2、用于控制整个类的测试用例的执行
cases=unittest.TestLoader().loadTestsFromTestCase(TestFixture.MyTestCase)
mysuit=unittest.TestSuite([cases])
mysuit.addTest(TestFixture.MyTestCase("test_anything"))#如果使用数据驱动，此方法不再适用，因为使用数据驱动，
                                                       # 生成的用例的名字是拼接的形式，而不是所定义的用例名字

myrunner=unittest.TextTestRunner(verbosity=2) #声明一个对象，并设置log输出级别
myrunner.run(mysuit) # 执行测试用例