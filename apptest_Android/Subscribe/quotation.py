from apptest_Android import APP_pre
from Script import wait
from Script.refresh import Refresh
import time
import toast
import random


class QuotationTest(APP_pre.LoginTest):
    # 订阅市场参考价
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
        wait.slide(self, text='订阅更多行情>>')
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath('//android.widget.TextView[@text="订阅更多行情>>"]').click()
        time.sleep(6)
        result = self.driver.find_element_by_xpath('//android.widget.TextView[@text="市场参考价"]').get_attribute('selected')
        self.assertEqual('true', result)
        self.driver.find_element_by_xpath('//*[@resource-id="com.zhongsu.online:id/recy"]/android.view.ViewGroup[1]').click()
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_id('com.zhongsu.online:id/tv_sub').click()
        time.sleep(6)
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
        self.assertIn(result, name.replace('\n', ''))
        self.driver.find_element_by_id('com.zhongsu.online:id/ib_back_layout_toolbar_back_righttv').click()
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath(
            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android'
            '.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout'
            '/androidx.viewpager.widget.ViewPager/androidx.recyclerview.widget.RecyclerView/android.widget'
            '.FrameLayout/android.widget.RelativeLayout/androidx.viewpager.widget.ViewPager/android.widget'
            '.RelativeLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.widget'
            '.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup['
            '1]/android.widget.RelativeLayout[1]/android.widget.ImageView').click()
        self.driver.find_element_by_id('com.zhongsu.online:id/check_sub').click()
        time.sleep(1)
        self.assertEqual('取消订阅成功', toast.get_toast_text(self, toast='取消订阅成功'))

# 订阅石化参考价
    def test_02(self):
        self.driver.find_element_by_xpath('//android.widget.TextView[@text="石化出厂价"]').click()
        self.driver.implicitly_wait(10)
        wait.slide(self, text='订阅更多行情>>')
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath('//android.widget.TextView[@text="订阅更多行情>>"]').click()
        time.sleep(6)
        result = self.driver.find_element_by_xpath('//android.widget.TextView[@text="石化出厂价"]').get_attribute('selected')
        self.assertEqual('true', result)
        self.driver.find_element_by_xpath(
            '//*[@resource-id="com.zhongsu.online:id/recy"]/android.view.ViewGroup[1]').click()
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_id('com.zhongsu.online:id/tv_sub').click()
        time.sleep(6)
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
        self.assertIn(result, name.replace('\n', ''))
        self.driver.find_element_by_id('com.zhongsu.online:id/ib_back_layout_toolbar_back_righttv').click()
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath(
            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android'
            '.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout'
            '/androidx.viewpager.widget.ViewPager/androidx.recyclerview.widget.RecyclerView/android.widget'
            '.FrameLayout/android.widget.RelativeLayout/androidx.viewpager.widget.ViewPager/android.widget'
            '.RelativeLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.widget'
            '.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup['
            '1]/android.widget.RelativeLayout[1]/android.widget.ImageView').click()
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_id('com.zhongsu.online:id/check_sub').click()
        time.sleep(1)
        self.assertEqual('取消订阅成功', toast.get_toast_text(self, toast='取消订阅成功'))

# 订阅国际价格行情
    def test_03(self):
        self.driver.find_element_by_xpath('//android.widget.TextView[@text="国际价格行情"]').click()
        self.driver.implicitly_wait(10)
        wait.slide(self, text='订阅更多行情>>')
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath('//android.widget.TextView[@text="订阅更多行情>>"]').click()
        time.sleep(6)
        result = self.driver.find_element_by_xpath('//android.widget.TextView[@text="国际价格行情"]').get_attribute('selected')
        self.assertEqual('true', result)
        self.driver.find_element_by_xpath(
            '//*[@resource-id="com.zhongsu.online:id/recy"]/android.view.ViewGroup[1]').click()
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_id('com.zhongsu.online:id/tv_sub').click()
        time.sleep(6)
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
        self.driver.find_element_by_xpath(
            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android'
            '.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout'
            '/androidx.viewpager.widget.ViewPager/androidx.recyclerview.widget.RecyclerView/android.widget'
            '.FrameLayout/android.widget.RelativeLayout/androidx.viewpager.widget.ViewPager/android.widget'
            '.RelativeLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.widget'
            '.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup['
            '1]/android.widget.RelativeLayout[1]/android.widget.ImageView').click()
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_id('com.zhongsu.online:id/check_sub').click()
        time.sleep(1)
        self.assertEqual('取消订阅成功', toast.get_toast_text(self, toast='取消订阅成功'))

# 订阅国际价格行情
    def test_04(self):
        self.driver.find_element_by_xpath('//android.widget.TextView[@text="基础石化原料"]').click()
        self.driver.implicitly_wait(10)
        wait.slide(self, text='订阅更多行情>>')
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath('//android.widget.TextView[@text="订阅更多行情>>"]').click()
        time.sleep(6)
        result = self.driver.find_element_by_xpath('//android.widget.TextView[@text="基础石化原料"]').get_attribute(
            'selected')
        self.assertEqual('true', result)
        self.driver.find_element_by_xpath(
            '//*[@resource-id="com.zhongsu.online:id/recy"]/android.view.ViewGroup[1]').click()
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_id('com.zhongsu.online:id/tv_sub').click()
        time.sleep(6)
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
        self.driver.find_element_by_xpath(
            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android'
            '.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout'
            '/androidx.viewpager.widget.ViewPager/androidx.recyclerview.widget.RecyclerView/android.widget'
            '.FrameLayout/android.widget.RelativeLayout/androidx.viewpager.widget.ViewPager/android.widget'
            '.RelativeLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.widget'
            '.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup['
            '1]/android.widget.RelativeLayout[1]/android.widget.ImageView').click()
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_id('com.zhongsu.online:id/check_sub').click()
        time.sleep(1)
        self.assertEqual('取消订阅成功', toast.get_toast_text(self, toast='取消订阅成功'))












