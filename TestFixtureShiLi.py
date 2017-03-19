#encoding:utf-8
import unittest
import time
from appium import webdriver

#测试登陆页面用例
class MyTestCase(unittest.TestCase):
    def setUp(self):
        """初始化测试数据"""
        desired_caps={} #
        desired_caps["platformName"]="Android" #测试的平台，android或者ios
        desired_caps["platformVesion"]="6.0"  #被测手机的系统的版本号
        desired_caps["deviceName"]="R8V7N15514000936" #测试手机的机型
        desired_caps["appPackage"]="com.jingwei.card" #测试app的包名
        desired_caps["appActivity"]="com.jingwei.card.LogoActivity" #启动app的activity名，可以通过appt查看
        desired_caps["unicodeKeyboard"]="True" #用来设置输入法，将输入法设置为unicode形式
        desired_caps["resetKeyboard"]="True" #恢复至原来的输入法

        self.driver=webdriver.Remote("http://localhost:4723/wd/hub",desired_caps)#利用appium启动app

        time.sleep(5)

    def test_something(self):
        """测试用例"""
        self.driver.find_element_by_id("email").send_keys("357637340@qq.com") #输入email
        self.driver.find_element_by_id("passwordET").send_keys("123456") #输入密码
        self.driver.find_element_by_id("loginButton").click()#点击登陆按钮

        try:
            if self.driver.find_element_by_id("loginButton").is_displayed(): #判断是否有email按钮来确定是否登陆成功
                exist=False
        except Exception,e:
            exist=True
        self.assertEqual(exist, False)

    def tearDown(self):
        """清除数据"""
        self.driver.quit() #资源释放

if __name__ == '__main__':
    unittest.main()
