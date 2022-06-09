from apptest_Android import APP_pre
import time
from Script import Mouse_keyboard
import toast
from selenium.webdriver.support.ui import WebDriverWait
from Script import wait
import random


class AppPublishTest(APP_pre.LoginTest):

    # 成功进入原料发布
    def test_01(self):
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_id('com.zhongsu.online:id/tv_publish_raw').click()
        self.driver.implicitly_wait(20)
        typ = self.driver.find_element_by_id('com.zhongsu.online:id/tv_quick_typeName').text
        self.assertEqual(typ, '（原料）')
        self.driver.find_element_by_id('com.zhongsu.online:id/btn_back').click()
        self.driver.implicitly_wait(20)

    # 成功进入改性发布
    def test_02(self):
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_id('com.zhongsu.online:id/tv_publish_ppo').click()
        self.driver.implicitly_wait(20)
        typ = self.driver.find_element_by_id('com.zhongsu.online:id/tv_quick_typeName').text
        self.assertEqual(typ, '（改性料）')
        self.driver.find_element_by_id('com.zhongsu.online:id/btn_back').click()
        self.driver.implicitly_wait(20)

    # 成功进入再生料发布
    def test_03(self):
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_id('com.zhongsu.online:id/tv_publish_reclaimed').click()
        self.driver.implicitly_wait(20)
        typ = self.driver.find_element_by_id('com.zhongsu.online:id/tv_type_name').text
        self.assertEqual(typ, '（再生料）')
        self.driver.find_element_by_id('com.zhongsu.online:id/btn_back').click()
        self.driver.implicitly_wait(20)

    # 成功进入助剂发布
    def test_04(self):
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_id('com.zhongsu.online:id/tv_publish_auxiliaries').click()
        self.driver.implicitly_wait(20)
        typ = self.driver.find_element_by_id('com.zhongsu.online:id/tv_type_name').text
        self.assertEqual(typ, '（助剂）')
        self.driver.find_element_by_id('com.zhongsu.online:id/btn_back').click()



