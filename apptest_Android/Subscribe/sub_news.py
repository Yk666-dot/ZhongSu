from apptest_Android import APP_pre
from Script import ElementExsit
import random
from Script.refresh import Refresh
import time
import toast
import random


class NewsTest(APP_pre.LoginTest):
    # 订阅资讯
    def test_01(self):
        # 我的订阅未登录需要跳转登录
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath('//*[@resource-id="com.zhongsu.online:id/tab_layout"]/android.widget'
                                          '.LinearLayout/android.widget.LinearLayout[2]').click()
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_id('com.zhongsu.online:id/to_login').click()
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_id('com.zhongsu.online:id/et_user_account').send_keys('18888648053')
        self.driver.find_element_by_id('com.zhongsu.online:id/btn_submit_login').click()
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_id('com.zhongsu.online:id/now_approve_tv').click()
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_id('com.zhongsu.online:id/tv_1').click()
        i = 1
        while i <= 6:
            self.driver.keyevent(13)
            i += 1
        time.sleep(3)
        self.driver.find_element_by_xpath(
            '//android.widget.LinearLayout[@content-desc="资讯"]/android.widget.TextView').click()
        time.sleep(3)
        while True:
            self.driver.find_element_by_id('com.zhongsu.online:id/tv_edit').click()
            self.driver.implicitly_wait(10)
            # 判断订阅管理是否有订阅标签，存在先清除所有标签，再订阅
            element = ElementExsit.is_element_exsit_xpath(self, xpath='//*[@resource-id="com.zhongsu.online:id/recy'
                                                                      '"]/android.widget.LinearLayout/android.view'
                                                                      '.ViewGroup/android.widget.CheckBox')
            if element is True:
                self.driver.find_element_by_xpath('//*[@resource-id="com.zhongsu.online:id/recy"]/android.widget'
                                              '.LinearLayout/android.view.ViewGroup/android.widget.CheckBox').click()
                self.driver.find_element_by_id('com.zhongsu.online:id/tv_cancel').click()
                self.driver.implicitly_wait(10)
                self.driver.find_element_by_id('com.zhongsu.online:id/last_approve_tv').click()
                time.sleep(3)
                self.driver.find_element_by_id('com.zhongsu.online:id/ib_back_layout_toolbar_back_righttv').click()
                self.driver.implicitly_wait(10)
            elif element is False:
                self.driver.find_element_by_id('com.zhongsu.online:id/ib_back_layout_toolbar_back_righttv').click()
                break
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_id('com.zhongsu.online:id/tv_add').click()
        self.driver.implicitly_wait(10)
        # 判断订阅成功
        el = self.driver.find_element_by_xpath('//*[@resource-id="com.zhongsu.online:id/recy"]/android.widget.FrameLayout[%s]' % random.randint(1, 20))
        el.click()
        label = el.text
        self.driver.find_element_by_id('com.zhongsu.online:id/tv_sub').click()
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_id('com.zhongsu.online:id/tv_all_labels').click()
        self.driver.implicitly_wait(10)
        result = self.driver.find_element_by_id('com.zhongsu.online:id/flow').text
        self.assertIn(label, result)








