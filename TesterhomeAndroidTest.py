#coding: utf-8
import os
import unittest
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class TesterhomeAndroidTest(unittest.TestCase):

    @classmethod
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = 'Android Emulator'
        desired_caps['app'] = PATH(
            './testerhome_1.0.apk'
        )
        desired_caps['appPackage'] = 'com.testerhome.android'
        desired_caps['appActivity'] = '.MainActivity'
        desired_caps['unicodeKeyboard'] = 'true'
        desired_caps['resetKeyboard'] = 'true'
        desired_caps['udid'] = 'b9e7dcad7d63'

        self.userName = 'TesterForTest'
        self.password = 'testerhome'
        
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        # 添加隐式等待
        self.driver.implicitly_wait(20)

    @classmethod
    def tearDown(self):
        self.driver.quit()

    def checkAlert(self):
        checkList = ['允许', '确认']
        for c in checkList:
            try:
                self.driver.find_element_by_id(c).click()
            except:
                pass

    def takeSreenShot(self):
        '''
        自动截图存到固定位置
        '''

    def myClick(self, obj):
        self.checkAlert()
        obj.click()
        self.takeSreenShot()

    def LoginByUserNameUiAutomatorMode(self):
        # 通过content-desc的方式获取menu控件并点击
        menuButton = self.driver.find_element_by_accessibility_id(u'打开导航菜单')
        menuButton.click()
        # self.myClick(menuButton)

        # 通过id的方式获取登录按钮并点击
        loginButton = self.driver.find_element_by_android_uiautomator(u'UiSelector().text("登录").className("android.widget.CheckedTextView")')
        loginButton.click()
        # self.myClick(loginButton)
        
        userEditView = self.driver.find_element_by_id('user_login')
        #userEditView = self.driver.find_element_by_accessibility_id(u'用户名 / Email') 

        userEditView.send_keys(self.userName)


        passwordEditView = self.driver.find_element_by_id('user_password')
        passwordEditView.send_keys(self.password)
        # sleep(2)
        confirmLoginBtn = self.driver.find_elements_by_accessibility_id(u'登录')[1]
        print(confirmLoginBtn.text)
        confirmLoginBtn.click()

        # 用显示等待来等待某个元素的出现，当作断言
        WebDriverWait(self.driver, 10).until(
            #lambda x: x.find_element_by_accessibility_id(u'搜索本站内容'), "Find element fail! Login Failed!"
            lambda x: x.find_element_by_android_uiautomator(u'UiSelector().text("搜索本站内容")'), "Find element fail! Login Failed!"
        )


    def testLoginByUserNameChromeDriverMode(self):
        # 过程详解（这里包含了chromedriver的知识点），方法名头部加上test就可以运行

        # 通过content-desc的方式获取menu控件并点击
        menuButton = self.driver.find_element_by_accessibility_id(u'打开导航菜单')
        menuButton.click()

        # 通过id的方式获取登录按钮并点击
        loginButton = self.driver.find_element_by_android_uiautomator(u'UiSelector().text("登录").className("android.widget.CheckedTextView")')
        loginButton.click()
        
        # <----  以下为webview页面
        # 一、通过content-desc获取webview中的控件信息
        #   这个方式的优点就是不需要考虑chromedriver，但是不同设备中，元素的信息会有所差异，不是特别稳定
        #userEditView = self.driver.find_element_by_accessibility_id(u'用户名 / Email')
        userEditView = self.driver.find_element_by_id('user_login')
        userEditView.send_keys(self.userName)

        # 二、通过chromedriver获取webview中的控件信息
        #   此步骤运行起来比较稳定，但是同样会有问题，设备限制>=4.4，apk中的webview必须打开debug模式，且手机需要安装google service和chrome浏览器
        # 具体操作：先要切换context到chromedriver中去
        # 1、获取当前的context上下文，得到所有上下文的list
        contexts = self.driver.contexts
        # 2、从list中找到当前app的webview_context
        for context in contexts:
            # 当context中包含webview或testerhome相关信息时，就切换到里面去
            print(context)
            if 'webview' in context.lower() and 'testerhome' in context.lower():
                self.driver.switch_to.context(context)
                break 
        # 3、使用webdriver的方式定位页面元素
        passwordEditView = self.driver.find_element_by_xpath('//*[@id="user_password"]')
        passwordEditView.send_keys(self.password)

        # 点击登录按钮
        self.driver.find_element_by_xpath('//*[@id="new_user"]/div[4]/input').click()
        #self.driver.find_elements_by_accessibility_id(u'登录')[1]

        # 如果点击登录后会跳转页面，建议把当前context切换回Native中去

        # for x in contexts:
        #     print("contexts="+x.lower())
        #     if 'native' in x.lower():
        #         nativeContextList =x
        #         print("nativeContext="+nativeContextList)

        #nativeContextList = contexts.filter(lambda x: 'native' in x.lower(), contexts)
        nativeContextList = list(filter(lambda x: 'native' in x.lower(), contexts))
        print(nativeContextList[0])
        nativeContextName = nativeContextList[0] if len(nativeContextList) != 0 else False
        if nativeContextName != False:
            self.driver.switch_to.context(nativeContextName)


        # 用显示等待来等待某个元素的出现，当作断言
        WebDriverWait(self.driver, 10).until(
            #lambda x: x.find_element_by_accessibility_id(u'搜索本站内容'), "Find element fail! Login Failed!"
            lambda x: x.find_element_by_android_uiautomator(u'UiSelector().text("搜索本站内容")'), "Find element fail! Login Failed!"
        )




if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TesterhomeAndroidTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
