from apptest_Android import APP_pre
import time
import toast
import random
# noinspection PyBroadException


class MyProvisionTest(APP_pre.LoginTest):
    # 测试无权限点击
    def test_01(self):
        # self.driver.implicitly_wait(20)
        # self.driver.find_element_by_xpath(
        #     '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout'
        #     '/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout'
        #     '/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.widget.LinearLayout[5]'
        #     '/android.widget.LinearLayout/android.widget.ImageView').click()
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_xpath('//android.widget.TextView[@text="可供产品"]').click()
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
        # self.driver.implicitly_wait(20)
        # self.driver.find_element_by_id('com.zhongsu.online:id/img_btn').click()
        # self.driver.implicitly_wait(20)
        # self.driver.find_element_by_id('com.zhongsu.online:id/img_btn').click()
        # self.driver.implicitly_wait(20)
        # self.driver.find_element_by_xpath(
        #     '//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[3]').click()
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_xpath('//android.widget.TextView[@text="可供产品"]').click()

    # 快速发布原料
    def test_02(self):
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_id('com.zhongsu.online:id/tv_publish').click()
        self.driver.implicitly_wait(20)
        type_name = self.driver.find_element_by_id('com.zhongsu.online:id/tv_type_name').text
        self.assertEqual(type_name, '原料')
        self.driver.find_element_by_id('com.zhongsu.online:id/tv_product_sel').click()
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_xpath('//*[@resource-id="com.zhongsu.online:id/recy_comb"]/android.widget'
                                          '.LinearLayout[1]/android.widget.CheckBox').click()
        self.driver.find_element_by_id('com.zhongsu.online:id/btn_confirm').click()
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_id('com.zhongsu.online:id/et_supplies').send_keys(11111)
        self.driver.find_element_by_id('com.zhongsu.online:id/btn_quick_publish').click()
        time.sleep(1)
        toast.get_toast_text(self, toast='发布成功')

    # 删除操作
    def test_03(self):
        name = self.driver.find_element_by_id('com.zhongsu.online:id/tv_name').text
        self.driver.find_element_by_id('com.zhongsu.online:id/tv_del').click()
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_id('com.zhongsu.online:id/now_approve_tv').click()
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_id('com.zhongsu.online:id/et_search').clear()
        self.driver.find_element_by_id('com.zhongsu.online:id/et_search').click()
        self.driver.find_element_by_id('com.zhongsu.online:id/et_search').send_keys(name)
        self.driver.press_keycode(66)
        self.driver.implicitly_wait(20)
        text = self.driver.find_element_by_id('com.zhongsu.online:id/empty_msg_text').text
        self.assertEqual('空空如也', text)

    # 快速发布改性
    def test_04(self):
        self.driver.find_element_by_xpath('//android.widget.TextView[@text="改性料"]').click()
        time.sleep(3)
        self.driver.find_element_by_id('com.zhongsu.online:id/tv_publish').click()
        self.driver.implicitly_wait(20)
        type_name = self.driver.find_element_by_id('com.zhongsu.online:id/tv_type_name').text
        self.assertEqual(type_name, '改性料')
        self.driver.find_element_by_id('com.zhongsu.online:id/tv_product_sel').click()
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_xpath('//*[@resource-id="com.zhongsu.online:id/recy_comb"]/android.widget'
                                          '.LinearLayout[1]/android.widget.CheckBox').click()
        self.driver.find_element_by_id('com.zhongsu.online:id/btn_confirm').click()
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_id('com.zhongsu.online:id/et_supplies').send_keys(11111)
        self.driver.find_element_by_id('com.zhongsu.online:id/btn_quick_publish').click()
        time.sleep(1)
        toast.get_toast_text(self, toast='发布成功')
        self.test_03()

    # 快速发布再生
    def test_05(self):
        self.driver.find_element_by_xpath('//android.widget.TextView[@text="再生料"]').click()
        time.sleep(3)
        self.driver.find_element_by_id('com.zhongsu.online:id/tv_publish').click()
        self.driver.implicitly_wait(20)
        type_name = self.driver.find_element_by_id('com.zhongsu.online:id/tv_type_name').text
        self.assertEqual(type_name, '再生料')
        self.driver.find_element_by_id('com.zhongsu.online:id/tv_product_sel').click()
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_xpath(
            '//*[@resource-id="com.zhongsu.online:id/grid_category_label"]/android.widget.Button[1]').click()
        self.driver.find_element_by_id('com.zhongsu.online:id/btn_confirm').click()
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_id('com.zhongsu.online:id/et_title_name').send_keys(random.randint(100, 9999))
        self.driver.find_element_by_id('com.zhongsu.online:id/tv_color').click()
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_xpath('//android.widget.TextView[@text="咖啡色"]').click()
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_id('com.zhongsu.online:id/tv_grade').click()
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_xpath('//android.widget.TextView[@text="特级"]').click()
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_id('com.zhongsu.online:id/tv_form').click()
        self.driver.find_element_by_xpath('//android.widget.TextView[@text="颗粒"]').click()
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_id('com.zhongsu.online:id/et_supplies').send_keys(11111)
        self.driver.find_element_by_id('com.zhongsu.online:id/btn_quick_publish').click()
        time.sleep(1)
        toast.get_toast_text(self, toast='发布成功')
        self.test_03()

    # 快速发布助剂
    def test_06(self):
        self.driver.find_element_by_xpath('//android.widget.TextView[@text="助剂"]').click()
        time.sleep(3)
        self.driver.find_element_by_id('com.zhongsu.online:id/tv_publish').click()
        self.driver.implicitly_wait(20)
        type_name = self.driver.find_element_by_id('com.zhongsu.online:id/tv_type_name').text
        self.assertEqual(type_name, '助剂')
        self.driver.find_element_by_id('com.zhongsu.online:id/tv_product_sel').click()
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_xpath(
            '//*[@resource-id="com.zhongsu.online:id/grid_category_label"]/android.widget.Button[1]').click()
        self.driver.find_element_by_id('com.zhongsu.online:id/btn_confirm').click()
        # 标题
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_id('com.zhongsu.online:id/et_title_name').send_keys(random.randint(100, 9999))
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_id('com.zhongsu.online:id/et_supplies').send_keys(11111)
        self.driver.find_element_by_id('com.zhongsu.online:id/btn_quick_publish').click()
        time.sleep(1)
        toast.get_toast_text(self, toast='发布成功')
        self.test_03()












