#encoding:utf-8
import unittest
import time
from appium import webdriver
from ddt import ddt,data,unpack

@ddt
class MyTestCase(unittest.TestCase):
    def setUp(self):
        """初始化测试数据"""
        desired_caps = {}  #
        desired_caps["platformName"] = "Android"  # 测试的平台，android或者ios
        desired_caps["platformVesion"] = "6.0"  # 被测手机的系统的版本号
        desired_caps["deviceName"] = "HUAWEI GRA-CL00"  # 测试手机的机型
        desired_caps["appPackage"] = "com.jingwei.card"  # 测试app的包名
        desired_caps["appActivity"] = "com.jingwei.card.LogoActivity"  # 启动app的activity名，可以通过appt查看
        desired_caps["unicodeKeyboard"] = "True"  # 手机键盘输入
        desired_caps["resetKeyboard"] = "True"  # 手机键盘输入

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)  # 利用appium启动app

        time.sleep(5)

    @data(("357637340@qq.com","123456","False"),
          ("12@12.com","1234567","True"))
    @unpack
    def test_something(self,username,password,result):
        """测试用例"""
        self.driver.find_element_by_id("email").send_keys(username)  # 输入email
        self.driver.find_element_by_id("passwordET").send_keys(password)  # 输入密码
        self.driver.find_element_by_id("loginButton").click()  # 点击登陆按钮

        try:
            if self.driver.find_element_by_id("loginButton").is_displayed():  # 判断是否有email按钮来确定是否登陆成功
                exist = False
        except Exception, e:
            exist = True
        self.assertEqual(exist, result)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
