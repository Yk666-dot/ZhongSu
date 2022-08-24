from apptest_Android import APP_pre
from Script import ElementExsit
from Script.login import login
from Script.refresh import Refresh
import time
import toast
from Script import refresh
import random
# self.driver.find_element_by_xpath('//android.widget.TextView[@text="改性料"]')


class QuotationTest(APP_pre.LoginTest):
    # 订阅商品
    def test_01(self):
        # 我的订阅未登录需要跳转登录
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_xpath('//*[@resource-id="com.zhongsu.online:id/tab_layout"]/android.widget'
                                          '.LinearLayout/android.widget.LinearLayout[5]').click()
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_xpath('//android.widget.TextView[@text="我的订阅"]').click()
        self.driver.implicitly_wait(5)
        login(self)
        self.driver.find_element_by_xpath('//android.widget.TextView[@text="我的订阅"]').click()
        self.driver.implicitly_wait(5)
        # self.driver.find_element_by_id('com.zhongsu.online:id/et_user_account').send_keys('18888648053')
        # self.driver.find_element_by_id('com.zhongsu.online:id/btn_submit_login').click()
        # self.driver.implicitly_wait(5)
        # self.driver.find_element_by_id('com.zhongsu.online:id/now_approve_tv').click()
        # self.driver.implicitly_wait(5)
        # self.driver.find_element_by_id('com.zhongsu.online:id/tv_1').click()
        # i = 1
        # while i <= 6:
        #     self.driver.keyevent(13)
        #     i += 1
        # self.driver.implicitly_wait(5)
        # self.driver.find_element_by_id('com.zhongsu.online:id/btn_confirm').click()
        # time.sleep(3)
        self.driver.find_element_by_xpath(
            '//android.widget.LinearLayout[@content-desc="商品"]/android.widget.TextView').click()

    # 订阅原料
    def test_02(self):
        time.sleep(3)
        while True:
            self.driver.find_element_by_id('com.zhongsu.online:id/tv_edit').click()
            self.driver.implicitly_wait(5)
            # 判断订阅管理是否有订阅商品，存在先清除所有商品，再订阅
            element = ElementExsit.is_element_exsit_xpath(self, xpath='//*[@resource-id="com.zhongsu.online:id/recy'
                                                                      '"]/android.widget.LinearLayout/android.view'
                                                                      '.ViewGroup/android.widget.CheckBox')
            print(element)
            if element is True:
                self.driver.find_element_by_xpath('//*[@resource-id="com.zhongsu.online:id/recy"]/android.widget'
                                                  '.LinearLayout/android.view.ViewGroup/android.widget.CheckBox').click()
                self.driver.find_element_by_id('com.zhongsu.online:id/tv_cancel').click()
                self.driver.implicitly_wait(5)
                self.driver.find_element_by_id('com.zhongsu.online:id/last_approve_tv').click()
                time.sleep(3)
                self.driver.find_element_by_id('com.zhongsu.online:id/ib_back_layout_toolbar_back_righttv').click()
                time.sleep(3)
                refresh.Refresh(self, x1=680, y1=738, y2=1428)
                time.sleep(3)
            elif element is False:
                self.driver.find_element_by_id('com.zhongsu.online:id/ib_back_layout_toolbar_back_righttv').click()
                break
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_id('com.zhongsu.online:id/tv_more').click()  # 点击订阅更多商品
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_xpath('//*[@resource-id="com.zhongsu.online:id/grid_product_symbol"]/android'
                                          '.widget.Button[1]').click()  # x选择产品符号
        self.driver.implicitly_wait(5)
        # 选择牌号
        self.driver.find_element_by_xpath('//*[@resource-id="com.zhongsu.online:id/rc_productlist"]/androidx'
                                          '.recyclerview.widget.RecyclerView[1]/android.widget.TextView[7]').click()
        self.driver.implicitly_wait(5)
        # 判断是否有情绪指数弹窗，有则先关闭
        element = ElementExsit.is_element_exsit_id(self, id='com.zhongsu.online:id/img_close')
        if element is True:
            self.driver.find_element_by_id('com.zhongsu.online:id/img_close').click()
        self.driver.implicitly_wait(5)
        i = 2
        while True:
            self.driver.find_element_by_xpath('//*[@resource-id="com.zhongsu.online:id/rc_productlist"]/android.widget'
                                              '.LinearLayout[%s]' % i).click()  # 点击第一个产品进入详情
            self.driver.implicitly_wait(5)
            element = ElementExsit.is_element_exsit_id(self, id='com.zhongsu.online:id/tv_back')
            # 判断该商品详情是否存在，存在则退出循环
            if element is True:
                self.driver.find_element_by_id('com.zhongsu.online:id/tv_back').click()  # 返回列表
                i += 1
            else:
                break
        text = self.driver.find_element_by_id('com.zhongsu.online:id/tv_sub').text  # 获取订阅按钮状态
        # 判断当前商品是已订阅还是未订阅
        if text == '订阅':
            self.driver.find_element_by_id('com.zhongsu.online:id/img_sub').click()
            time.sleep(1)
            self.assertEqual('订阅成功', toast.get_toast_text(self, toast='订阅成功'))
        else:
            self.driver.find_element_by_id('com.zhongsu.online:id/img_sub').click()
            self.driver.implicitly_wait(5)
            self.driver.find_element_by_id('com.zhongsu.online:id/now_approve_tv').click()
            time.sleep(1)
            self.assertEqual('取消成功', toast.get_toast_text(self, toast='取消成功'))
            self.driver.find_element_by_id('com.zhongsu.online:id/img_sub').click()
            time.sleep(1)
            self.assertEqual('订阅成功', toast.get_toast_text(self, toast='订阅成功'))
        i = 1
        while i <= 4:
            self.driver.back()
            time.sleep(1)
            i += 1

        # 订阅改性料
    def test_03(self):
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_xpath('//android.widget.TextView[@text="改性料"]').click()
        self.driver.implicitly_wait(5)
        # 进入订阅管理
        while True:
            self.driver.find_element_by_id('com.zhongsu.online:id/tv_edit').click()
            self.driver.implicitly_wait(5)
            # 判断订阅管理是否有订阅商品，存在先清除所有商品，再订阅
            element = ElementExsit.is_element_exsit_xpath(self, xpath='//*[@resource-id="com.zhongsu.online:id/recy'
                                                                      '"]/android.widget.LinearLayout/android.view'
                                                                      '.ViewGroup/android.widget.CheckBox')
            if element is True:
                self.driver.find_element_by_xpath('//*[@resource-id="com.zhongsu.online:id/recy"]/android.widget'
                                                  '.LinearLayout/android.view.ViewGroup/android.widget.CheckBox').click()
                self.driver.find_element_by_id('com.zhongsu.online:id/tv_cancel').click()
                self.driver.implicitly_wait(5)
                self.driver.find_element_by_id('com.zhongsu.online:id/last_approve_tv').click()
                time.sleep(3)
                self.driver.find_element_by_id('com.zhongsu.online:id/ib_back_layout_toolbar_back_righttv').click()
                time.sleep(3)
                refresh.Refresh(self, x1=680, y1=738, y2=1428)
                time.sleep(3)
            elif element is False:
                self.driver.find_element_by_id('com.zhongsu.online:id/ib_back_layout_toolbar_back_righttv').click()
                break
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_id('com.zhongsu.online:id/tv_more').click()  # 点击订阅更多商品
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_xpath('//*[@resource-id="com.zhongsu.online:id/grid_product_symbol"]/android'
                                          '.widget.Button[1]').click()  # x选择产品符号
        self.driver.implicitly_wait(5)
        # 选择牌号
        self.driver.find_element_by_xpath('//*[@resource-id="com.zhongsu.online:id/rc_productlist"]/androidx'
                                          '.recyclerview.widget.RecyclerView[1]/android.widget.TextView[1]').click()
        self.driver.implicitly_wait(5)
        # 判断是否有情绪指数弹窗，有则先关闭
        element = ElementExsit.is_element_exsit_id(self, id='com.zhongsu.online:id/img_close')
        if element is True:
            self.driver.find_element_by_id('com.zhongsu.online:id/img_close').click()
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_id('com.zhongsu.online:id/item_good').click()
        self.driver.implicitly_wait(5)
        text = self.driver.find_element_by_id('com.zhongsu.online:id/tv_sub').text  # 获取订阅按钮状态
        # 判断当前商品是已订阅还是未订阅
        if text == '订阅':
            self.driver.find_element_by_id('com.zhongsu.online:id/img_sub').click()
            time.sleep(1)
            self.assertEqual('订阅成功', toast.get_toast_text(self, toast='订阅成功'))
        else:
            self.driver.find_element_by_id('com.zhongsu.online:id/img_sub').click()
            self.driver.implicitly_wait(5)
            self.driver.find_element_by_id('com.zhongsu.online:id/now_approve_tv').click()
            time.sleep(1)
            self.assertEqual('取消成功', toast.get_toast_text(self, toast='取消成功'))
            self.driver.find_element_by_id('com.zhongsu.online:id/img_sub').click()
            time.sleep(1)
            self.assertEqual('订阅成功', toast.get_toast_text(self, toast='订阅成功'))
        # 返回订阅列表
        i = 1
        while i <= 4:
            self.driver.back()
            time.sleep(1)
            i += 1

    # 订阅再生料
    def test_04(self):
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_xpath('//android.widget.TextView[@text="再生料"]').click()
        self.driver.implicitly_wait(5)
        # 进入订阅管理
        while True:
            self.driver.find_element_by_id('com.zhongsu.online:id/tv_edit').click()
            self.driver.implicitly_wait(5)
            # 判断订阅管理是否有订阅商品，存在先清除所有商品，再订阅
            element = ElementExsit.is_element_exsit_xpath(self,
                                                          xpath='//*[@resource-id="com.zhongsu.online:id/recy'
                                                                '"]/android.widget.LinearLayout/android.view'
                                                                '.ViewGroup/android.widget.CheckBox')
            if element is True:
                self.driver.find_element_by_xpath(
                    '//*[@resource-id="com.zhongsu.online:id/recy"]/android.widget'
                    '.LinearLayout/android.view.ViewGroup/android.widget.CheckBox').click()
                self.driver.find_element_by_id('com.zhongsu.online:id/tv_cancel').click()
                self.driver.implicitly_wait(5)
                self.driver.find_element_by_id('com.zhongsu.online:id/last_approve_tv').click()
                time.sleep(3)
                self.driver.find_element_by_id(
                    'com.zhongsu.online:id/ib_back_layout_toolbar_back_righttv').click()
                time.sleep(3)
                refresh.Refresh(self, x1=680, y1=738, y2=1428)
                time.sleep(3)
            elif element is False:
                self.driver.find_element_by_id(
                    'com.zhongsu.online:id/ib_back_layout_toolbar_back_righttv').click()
                break
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_id('com.zhongsu.online:id/tv_more').click()  # 点击订阅更多商品
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_xpath(
            '//*[@resource-id="com.zhongsu.online:id/grid_product_symbol"]/android'
            '.widget.Button[1]').click()  # x选择产品符号
        self.driver.implicitly_wait(5)
        self.driver.find_elements_by_id('com.zhongsu.online:id/linearLayout5')[0].click()
        self.driver.implicitly_wait(5)
        text = self.driver.find_element_by_id('com.zhongsu.online:id/tv_sub').text  # 获取订阅按钮状态
        # 判断当前商品是已订阅还是未订阅
        if text == '订阅':
            self.driver.find_element_by_id('com.zhongsu.online:id/img_sub').click()
            time.sleep(1)
            self.assertEqual('订阅成功', toast.get_toast_text(self, toast='订阅成功'))
        else:
            self.driver.find_element_by_id('com.zhongsu.online:id/img_sub').click()
            self.driver.implicitly_wait(5)
            self.driver.find_element_by_id('com.zhongsu.online:id/now_approve_tv').click()
            time.sleep(1)
            self.assertEqual('取消成功', toast.get_toast_text(self, toast='取消成功'))
            self.driver.find_element_by_id('com.zhongsu.online:id/img_sub').click()
            time.sleep(1)
            self.assertEqual('订阅成功', toast.get_toast_text(self, toast='订阅成功'))
        # 返回订阅列表
        i = 1
        while i <= 3:
            self.driver.back()
            time.sleep(1)
            i += 1

# 订阅助剂
    def test_05(self):
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_xpath('//android.widget.TextView[@text="助剂"]').click()
        self.driver.implicitly_wait(5)
        # 进入订阅管理
        while True:
            self.driver.find_element_by_id('com.zhongsu.online:id/tv_edit').click()
            self.driver.implicitly_wait(5)
            # 判断订阅管理是否有订阅商品，存在先清除所有商品，再订阅
            element = ElementExsit.is_element_exsit_xpath(self,
                                                          xpath='//*[@resource-id="com.zhongsu.online:id/recy'
                                                                '"]/android.widget.LinearLayout/android.view'
                                                                '.ViewGroup/android.widget.CheckBox')
            if element is True:
                self.driver.find_element_by_xpath(
                    '//*[@resource-id="com.zhongsu.online:id/recy"]/android.widget'
                    '.LinearLayout/android.view.ViewGroup/android.widget.CheckBox').click()
                self.driver.find_element_by_id('com.zhongsu.online:id/tv_cancel').click()
                self.driver.implicitly_wait(5)
                self.driver.find_element_by_id('com.zhongsu.online:id/last_approve_tv').click()
                time.sleep(3)
                self.driver.find_element_by_id(
                    'com.zhongsu.online:id/ib_back_layout_toolbar_back_righttv').click()
                time.sleep(3)
                refresh.Refresh(self, x1=680, y1=738, y2=1428)
                time.sleep(3)
            elif element is False:
                self.driver.find_element_by_id(
                    'com.zhongsu.online:id/ib_back_layout_toolbar_back_righttv').click()
                break
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_id('com.zhongsu.online:id/tv_more').click()  # 点击订阅更多商品
        for i in range(1, 32):
            self.driver.implicitly_wait(5)
            self.driver.find_element_by_xpath(
                '//*[@resource-id="com.zhongsu.online:id/grid_product_symbol"]/android'
                '.widget.Button[%s]' % i).click()  # x选择产品符号
            self.driver.implicitly_wait(5)
            elements = self.driver.find_elements_by_id('com.zhongsu.online:id/linearLayout5')
            print('elements:%s' % len(elements))
            # 判断列表是否有商品，没有返回选择新的产品符号
            if len(elements) == 0:
                print('%s:供应列表没有商品' % i)
                self.driver.back()

            else:
                self.driver.find_elements_by_id('com.zhongsu.online:id/linearLayout5')[0].click()
                self.driver.implicitly_wait(5)
                text = self.driver.find_element_by_id('com.zhongsu.online:id/tv_sub').text  # 获取订阅按钮状态
                # 判断当前商品是已订阅还是未订阅
                if text == '订阅':
                    self.driver.find_element_by_id('com.zhongsu.online:id/img_sub').click()
                    time.sleep(1)
                    self.assertEqual('订阅成功', toast.get_toast_text(self, toast='订阅成功'))
                else:
                    self.driver.find_element_by_id('com.zhongsu.online:id/img_sub').click()
                    self.driver.implicitly_wait(5)
                    self.driver.find_element_by_id('com.zhongsu.online:id/now_approve_tv').click()
                    time.sleep(1)
                    self.assertEqual('取消成功', toast.get_toast_text(self, toast='取消成功'))
                    self.driver.find_element_by_id('com.zhongsu.online:id/img_sub').click()
                    time.sleep(1)
                    self.assertEqual('订阅成功', toast.get_toast_text(self, toast='订阅成功'))
                # 返回订阅列表
                i = 1
                while i <= 3:
                    self.driver.back()
                    time.sleep(1)
                    i += 1
                break




        # wait.slide(self, text='更多商品')
        # self.driver.find_element_by_xpath('//android.widget.TextView[@text="更多商品>>"]').click()
        # time.sleep(6)
        # result = self.driver.find_element_by_xpath('//android.widget.TextView[@text="市场参考价"]').get_attribute('selected')
        # self.assertEqual('true', result)
        # self.driver.find_element_by_xpath('//*[@resource-id="com.zhongsu.online:id/recy"]/android.view.ViewGroup[1]').click()
        # self.driver.implicitly_wait(20)
        # self.driver.find_element_by_id('com.zhongsu.online:id/tv_sub').click()
        # time.sleep(6)
        # result = self.driver.find_element_by_id('com.zhongsu.online:id/tv_sub').text
        # if result == '订阅':
        #     self.driver.find_element_by_id('com.zhongsu.online:id/tv_sub').click()
        #     result = self.driver.find_element_by_id('com.zhongsu.online:id/tv_sub').text
        # self.assertEqual('已订阅', result)
        # name = self.driver.find_element_by_id('com.zhongsu.online:id/tv_market_title').text
        # 返回订阅列表，取消订阅