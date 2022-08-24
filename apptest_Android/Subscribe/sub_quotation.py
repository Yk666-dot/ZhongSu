from apptest_Android import APP_pre
from Script import wait
from Script.refresh import Refresh
from Script.ElementExsit import is_element_exsit_xpath
from Script import refresh
import time
import toast
import random


class QuotationTest(APP_pre.LoginTest):
    # 订阅市场参考价
    def test_01(self):
        # 我的订阅未登录需要跳转登录
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath('//*[@resource-id="com.zhongsu.online:id/tab_layout"]/android.widget'
                                          '.LinearLayout/android.widget.LinearLayout[5]').click()
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_xpath('//android.widget.TextView[@text="我的订阅"]').click()
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
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_id('com.zhongsu.online:id/btn_confirm').click()
        time.sleep(3)
        self.driver.find_element_by_xpath('//android.widget.TextView[@text="我的订阅"]').click()
        self.driver.implicitly_wait(5)
        while True:
            self.driver.find_element_by_id('com.zhongsu.online:id/tv_edit').click()
            self.driver.implicitly_wait(10)
            # 判断订阅管理是否有订阅标签，存在先清除所有标签，再订阅
            element = is_element_exsit_xpath(self, xpath='//*[@resource-id="com.zhongsu.online:id/recy'
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
                time.sleep(3)
                refresh.Refresh(self, x1=680, y1=738, y2=1428)
                time.sleep(3)
            elif element is False:
                self.driver.find_element_by_id('com.zhongsu.online:id/ib_back_layout_toolbar_back_righttv').click()
                break
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath('//android.widget.TextView[@text="订阅更多行情>>"]').click()
        time.sleep(6)
        # 判断选中的是市场参考价
        result = self.driver.find_element_by_xpath('//android.widget.TextView[@text="市场参考价"]').get_attribute('selected')
        self.assertEqual('true', result)
        # 选择进入参考价详情，点击订阅
        self.driver.find_element_by_xpath('//*[@resource-id="com.zhongsu.online:id/recy"]/android.view.ViewGroup[1]').click()
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_id('com.zhongsu.online:id/tv_sub').click()
        time.sleep(3)
        result = self.driver.find_element_by_id('com.zhongsu.online:id/tv_sub').text
        # 判断是不是已订阅的状态
        if result == '订阅':
            self.driver.find_element_by_id('com.zhongsu.online:id/tv_sub').click()
            result = self.driver.find_element_by_id('com.zhongsu.online:id/tv_sub').text
        self.assertEqual('已订阅', result)
        name = self.driver.find_element_by_id('com.zhongsu.online:id/tv_market_title').text
        # 返回订阅列表
        self.driver.find_element_by_id('com.zhongsu.online:id/img_back').click()
        time.sleep(3)
        self.driver.find_element_by_id('com.zhongsu.online:id/img_back').click()
        time.sleep(3)
        Refresh(self, x1=538, y1=706, y2=1546)  # 刷新列表显示最新订阅
        time.sleep(3)
        self.driver.find_element_by_id('com.zhongsu.online:id/tv_edit').click()
        self.driver.implicitly_wait(10)
        # 取消订阅
        i = len(self.driver.find_elements_by_xpath(
            '//*[@resource-id="com.zhongsu.online:id/recy"]/android.view.ViewGroup'))
        result = self.driver.find_element_by_xpath(
            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android'
            '.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup['
            '2]/android.widget.RelativeLayout[2]/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup['
            '%s]/android.widget.TextView[1]' % i).text
        self.assertIn(result, name.replace('\n', ''))
        self.driver.find_element_by_id('com.zhongsu.online:id/ib_back_layout_toolbar_back_righttv').click()
        self.driver.implicitly_wait(10)
        self.driver.find_elements_by_id('com.zhongsu.online:id/rel_arrow')[0].click()
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_id('com.zhongsu.online:id/check_sub').click()
        time.sleep(1)
        self.assertEqual('取消订阅成功', toast.get_toast_text(self, toast='取消订阅成功'))

# 订阅石化参考价
    def test_02(self):
        self.driver.find_element_by_xpath('//android.widget.TextView[@text="石化出厂价"]').click()
        self.driver.implicitly_wait(10)
        while True:
            self.driver.find_element_by_id('com.zhongsu.online:id/tv_edit').click()
            self.driver.implicitly_wait(10)
            # 判断订阅管理是否有订阅标签，存在先清除所有标签，再订阅
            element = is_element_exsit_xpath(self, xpath='//*[@resource-id="com.zhongsu.online:id/recy'
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
                time.sleep(3)
                refresh.Refresh(self, x1=680, y1=738, y2=1428)
                time.sleep(3)
            elif element is False:
                self.driver.find_element_by_id('com.zhongsu.online:id/ib_back_layout_toolbar_back_righttv').click()
                break
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath('//android.widget.TextView[@text="订阅更多行情>>"]').click()
        time.sleep(3)
        # 判断进入石化出厂价列表
        result = self.driver.find_element_by_xpath('//android.widget.TextView[@text="石化出厂价"]').get_attribute('selected')
        self.assertEqual('true', result)
        # 进入详情，点击订阅
        self.driver.find_element_by_xpath(
            '//*[@resource-id="com.zhongsu.online:id/recy"]/android.view.ViewGroup[1]').click()
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_id('com.zhongsu.online:id/tv_sub').click()
        time.sleep(3)
        # 判断是否状态为已订阅
        result = self.driver.find_element_by_id('com.zhongsu.online:id/tv_sub').text
        if result == '订阅':
            self.driver.find_element_by_id('com.zhongsu.online:id/tv_sub').click()
            result = self.driver.find_element_by_id('com.zhongsu.online:id/tv_sub').text
        self.assertEqual('已订阅', result)
        name = self.driver.find_element_by_id('com.zhongsu.online:id/tv_market_title').text
        # 返回订阅列表，取消订阅
        self.driver.find_element_by_id('com.zhongsu.online:id/img_back').click()
        time.sleep(3)
        self.driver.find_element_by_id('com.zhongsu.online:id/img_back').click()
        time.sleep(3)
        Refresh(self, x1=538, y1=706, y2=1546)  # 刷新订阅列表
        time.sleep(3)
        self.driver.find_element_by_id('com.zhongsu.online:id/tv_edit').click()
        self.driver.implicitly_wait(10)
        i = len(self.driver.find_elements_by_xpath(
            '//*[@resource-id="com.zhongsu.online:id/recy"]/android.view.ViewGroup'))
        result = self.driver.find_element_by_xpath(
            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android'
            '.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup['
            '2]/android.widget.RelativeLayout[2]/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup['
            '%s]/android.widget.TextView[1]' % i).text
        self.assertIn(result, name.replace('\n', ''))
        self.driver.find_element_by_id('com.zhongsu.online:id/ib_back_layout_toolbar_back_righttv').click()
        self.driver.implicitly_wait(10)
        self.driver.find_elements_by_id('com.zhongsu.online:id/rel_arrow')[0].click()
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_id('com.zhongsu.online:id/check_sub').click()
        time.sleep(1)
        self.assertEqual('取消订阅成功', toast.get_toast_text(self, toast='取消订阅成功'))

# 订阅国际价格行情
    def test_03(self):
        self.driver.find_element_by_xpath('//android.widget.TextView[@text="国际价格行情"]').click()
        self.driver.implicitly_wait(10)
        while True:
            self.driver.find_element_by_id('com.zhongsu.online:id/tv_edit').click()
            self.driver.implicitly_wait(10)
            # 判断订阅管理是否有订阅标签，存在先清除所有标签，再订阅
            element = is_element_exsit_xpath(self, xpath='//*[@resource-id="com.zhongsu.online:id/recy'
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
                time.sleep(3)
                refresh.Refresh(self, x1=680, y1=738, y2=1428)
                time.sleep(3)
            elif element is False:
                self.driver.find_element_by_id('com.zhongsu.online:id/ib_back_layout_toolbar_back_righttv').click()
                break
        self.driver.implicitly_wait(10)
        wait.slide(self, text='订阅更多行情>>')
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath('//android.widget.TextView[@text="订阅更多行情>>"]').click()
        time.sleep(3)
        result = self.driver.find_element_by_xpath('//android.widget.TextView[@text="国际价格行情"]').get_attribute('selected')
        self.assertEqual('true', result)  # 判断进入国际价格行情列表
        self.driver.find_element_by_xpath(
            '//*[@resource-id="com.zhongsu.online:id/recy"]/android.view.ViewGroup[1]').click()  # 进入详情
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_id('com.zhongsu.online:id/tv_sub').click()
        time.sleep(3)
        # 判断订阅按钮状态正确
        result = self.driver.find_element_by_id('com.zhongsu.online:id/tv_sub').text
        if result == '订阅':
            self.driver.find_element_by_id('com.zhongsu.online:id/tv_sub').click()
            result = self.driver.find_element_by_id('com.zhongsu.online:id/tv_sub').text
        self.assertEqual('已订阅', result)
        name = self.driver.find_element_by_id('com.zhongsu.online:id/tv_market_title').text
        # 返回订阅列表，取消订阅
        self.driver.find_element_by_id('com.zhongsu.online:id/img_back').click()
        time.sleep(6)
        self.driver.find_element_by_id('com.zhongsu.online:id/img_back').click()
        time.sleep(6)
        Refresh(self, x1=538, y1=706, y2=1546)
        time.sleep(3)
        self.driver.find_element_by_id('com.zhongsu.online:id/tv_edit').click()
        self.driver.implicitly_wait(10)
        i = len(self.driver.find_elements_by_xpath(
            '//*[@resource-id="com.zhongsu.online:id/recy"]/android.view.ViewGroup'))
        result = self.driver.find_element_by_xpath(
            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android'
            '.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup['
            '2]/android.widget.RelativeLayout[2]/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup['
            '%s]/android.widget.TextView[1]' % i).text
        name = name.replace('\n', '')
        self.assertIn(name.replace('/', ' '), result)
        self.driver.find_element_by_id('com.zhongsu.online:id/ib_back_layout_toolbar_back_righttv').click()
        self.driver.implicitly_wait(10)
        self.driver.find_elements_by_id('com.zhongsu.online:id/rel_arrow')[0].click()
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_id('com.zhongsu.online:id/check_sub').click()
        time.sleep(1)
        self.assertEqual('取消订阅成功', toast.get_toast_text(self, toast='取消订阅成功'))

# 订阅基础石化原料
    def test_04(self):
        self.driver.find_element_by_xpath('//android.widget.TextView[@text="基础石化原料"]').click()
        self.driver.implicitly_wait(10)
        while True:
            self.driver.find_element_by_id('com.zhongsu.online:id/tv_edit').click()
            self.driver.implicitly_wait(10)
            # 判断订阅管理是否有订阅标签，存在先清除所有标签，再订阅
            element = is_element_exsit_xpath(self, xpath='//*[@resource-id="com.zhongsu.online:id/recy'
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
                time.sleep(3)
                refresh.Refresh(self, x1=680, y1=738, y2=1428)
                time.sleep(3)
            elif element is False:
                self.driver.find_element_by_id('com.zhongsu.online:id/ib_back_layout_toolbar_back_righttv').click()
                break
        self.driver.implicitly_wait(10)
        wait.slide(self, text='订阅更多行情>>')
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath('//android.widget.TextView[@text="订阅更多行情>>"]').click()
        time.sleep(3)
        result = self.driver.find_element_by_xpath('//android.widget.TextView[@text="基础石化原料"]').get_attribute(
            'selected')
        self.assertEqual('true', result)  # 判断进入基础石化原料列表
        self.driver.find_element_by_xpath(
            '//*[@resource-id="com.zhongsu.online:id/recy"]/android.view.ViewGroup[1]').click()
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_id('com.zhongsu.online:id/tv_sub').click()
        time.sleep(3)
        # 判断订阅按钮状态
        result = self.driver.find_element_by_id('com.zhongsu.online:id/tv_sub').text
        if result == '订阅':
            self.driver.find_element_by_id('com.zhongsu.online:id/tv_sub').click()
            result = self.driver.find_element_by_id('com.zhongsu.online:id/tv_sub').text
        self.assertEqual('已订阅', result)
        name = self.driver.find_element_by_id('com.zhongsu.online:id/tv_market_title').text
        # 返回订阅列表，取消订阅
        self.driver.find_element_by_id('com.zhongsu.online:id/img_back').click()
        time.sleep(3)
        self.driver.find_element_by_id('com.zhongsu.online:id/img_back').click()
        time.sleep(3)
        Refresh(self, x1=538, y1=706, y2=1546)
        time.sleep(3)
        self.driver.find_element_by_id('com.zhongsu.online:id/tv_edit').click()
        self.driver.implicitly_wait(10)
        i = len(self.driver.find_elements_by_xpath(
            '//*[@resource-id="com.zhongsu.online:id/recy"]/android.view.ViewGroup'))
        result = self.driver.find_element_by_xpath(
            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android'
            '.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup['
            '2]/android.widget.RelativeLayout[2]/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup['
            '%s]/android.widget.TextView[1]' % i).text
        name = name.replace('\n', '')
        self.assertIn(name.replace('/', ' '), result)
        self.driver.find_element_by_id('com.zhongsu.online:id/ib_back_layout_toolbar_back_righttv').click()
        self.driver.implicitly_wait(10)
        self.driver.find_elements_by_id('com.zhongsu.online:id/rel_arrow')[0].click()
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_id('com.zhongsu.online:id/check_sub').click()
        time.sleep(1)
        self.assertEqual('取消订阅成功', toast.get_toast_text(self, toast='取消订阅成功'))












