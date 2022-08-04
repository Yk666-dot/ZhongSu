from apptest_Android import APP_pre
import time


class AttestationTest(APP_pre.LoginTest):
    # 测试无权限点击
    def test_01(self):
        self.driver.find_element_by_xpath('//android.widget.TextView[@text="企业认证"]').click()
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_id('com.zhongsu.online:id/et_user_account').send_keys('18888648053')
        self.driver.find_element_by_id('com.zhongsu.online:id/btn_submit_login').click()
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_id('com.zhongsu.online:id/now_approve_tv').click()
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_id('com.zhongsu.online:id/tv_1').click()
        i = 1
        while i <= 6:
            self.driver.keyevent(13)
            i += 1

    # 测试企业基本信息和工商信息返回企业认证
    def test_02(self):
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_xpath('//android.widget.TextView[@text="企业认证"]').click()
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_id('com.zhongsu.online:id/layout_auth_info').click()
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_id('com.zhongsu.online:id/btn_next_to_business').click()
        time.sleep(3)
        self.driver.find_element_by_id('com.zhongsu.online:id/ib_back_layout_toolbar_back_righttv').click()
        time.sleep(3)
        self.driver.find_element_by_id('com.zhongsu.online:id/ib_back_layout_toolbar_back_righttv').click()
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_id('com.zhongsu.online:id/now_approve_tv').click()
        self.driver.implicitly_wait(20)
        title = self.driver.find_element_by_id('com.zhongsu.online:id/toolbar_title_layout_toolbar_back_righttv').text
        self.assertEqual('企业认证', title)

    # 输入选择框点击展开返回
    def test_03(self):
        self.driver.find_element_by_id('com.zhongsu.online:id/layout_auth_info').click()
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_id('com.zhongsu.online:id/tv_co_identities').click()
        self.driver.implicitly_wait(20)
        title = self.driver.find_element_by_id('com.zhongsu.online:id/title_tv').text
        self.assertEqual('企业身份', title)
        self.driver.find_element_by_id('com.zhongsu.online:id/left_tv').click()
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_id('com.zhongsu.online:id/tv_co_business_model').click()
        self.driver.implicitly_wait(20)
        title = self.driver.find_element_by_id('com.zhongsu.online:id/title_tv').text
        self.assertEqual('经营模式', title)
        self.driver.find_element_by_id('com.zhongsu.online:id/left_tv').click()
        self.driver.implicitly_wait(20)









