from apptest import APP_pre
import time
from Script import ScreenShot
from Script import Mouse_keyboard
import toast
from selenium.webdriver.support.ui import WebDriverWait
import sys
from Script import wait
import random
# noinspection PyBroadException


class SalesManagementTest(APP_pre.LoginTest):

    # 设置log, 这里使用默认log
    # def log(self):
    #     logging.basicConfig(
    #         level=logging.INFO,
    #         format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
    #         datefmt='[%Y-%m_%d %H:%M:%S]',
    #         filename=r'C:\Users\msi\Pictures\Saved Pictures\log\%s.log' % self,
    #         filemode='a')

    # 未登录点击销售商品,跳转登录
    def test_01(self):
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_xpath(
            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout'
            '/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout'
            '/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.widget.LinearLayout[5]'
            '/android.widget.LinearLayout/android.widget.ImageView').click()
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_id('com.zhongsu.online:id/btn_my_supply').click()
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

    # 切换分类
    def test_02(self):
        # SalesManagementTest.log(self='SalesManagementTest')
        try:
            self.driver.implicitly_wait(20)
            self.driver.find_element_by_id('com.zhongsu.online:id/btn_my_supply').click()
            self.driver.implicitly_wait(20)
            text = self.driver.find_element_by_xpath(
                '//*[@resource-id="com.zhongsu.online:id/rc_newslist"]/android.view.ViewGroup['
                '1]/android.widget.LinearLayout[1]/android.widget.TextView').text
            # 切改性料
            self.driver.find_element_by_xpath(
                '//android.widget.LinearLayout[@content-desc="改性料"]/android.widget.TextView').click()
            time.sleep(3)
            actual = self.driver.find_element_by_xpath(
                '//*[@resource-id="com.zhongsu.online:id/rc_newslist"]/android.view.ViewGroup['
                '1]/android.widget.LinearLayout[1]/android.widget.TextView').text
            self.assertNotIn(text, actual)
            # 切再生料
            self.driver.find_element_by_xpath(
                '//android.widget.LinearLayout[@content-desc="再生料"]/android.widget.TextView').click()
            time.sleep(3)
            actual = self.driver.find_element_by_xpath(
                '//*[@resource-id="com.zhongsu.online:id/rc_newslist"]/android.view.ViewGroup['
                '1]/android.widget.LinearLayout[1]/android.widget.TextView').text
            self.assertNotIn(text, actual)
            # 切助剂
            self.driver.find_element_by_xpath(
                '//android.widget.LinearLayout[@content-desc="助剂"]/android.widget.TextView').click()
            time.sleep(3)
            actual = self.driver.find_element_by_xpath(
                '//*[@resource-id="com.zhongsu.online:id/rc_newslist"]/android.view.ViewGroup['
                '1]/android.widget.LinearLayout[1]/android.widget.TextView').text
            self.assertNotIn(text, actual)
            # 切原料
            self.driver.find_element_by_xpath(
                '//android.widget.LinearLayout[@content-desc="原料"]/android.widget.TextView').click()
            time.sleep(3)
            actual = self.driver.find_element_by_xpath(
                '//*[@resource-id="com.zhongsu.online:id/rc_newslist"]/android.view.ViewGroup['
                '1]/android.widget.LinearLayout[1]/android.widget.TextView').text
            self.assertEqual(text, actual)
        except Exception as _:
            f_name = sys._getframe().f_code.co_name  # 获取正在执行的函数名
            ScreenShot.getScreenShot(self, file="SalesManagementTest", case=f_name)

    # 搜索和筛选
    def test_03(self):
        try:
            text = self.driver.find_element_by_xpath(
                '//*[@resource-id="com.zhongsu.online:id/rc_newslist"]/android.view.ViewGroup['
                '2]/android.widget.LinearLayout[1]/android.widget.TextView').text
            # 搜索存在的商品
            self.driver.find_element_by_id('com.zhongsu.online:id/et_search').click()
            self.driver.find_element_by_id('com.zhongsu.online:id/et_search').send_keys(text)
            self.driver.press_keycode(66)
            time.sleep(3)
            num = self.driver.find_elements_by_xpath(
                '//*[@resource-id="com.zhongsu.online:id/rc_newslist"]/android.view.ViewGroup')
            self.assertEqual(1, len(num))
            actual = self.driver.find_element_by_xpath(
                '//*[@resource-id="com.zhongsu.online:id/rc_newslist"]/android.view.ViewGroup['
                '1]/android.widget.LinearLayout[1]/android.widget.TextView').text
            self.assertEqual(text, actual)
            # 搜索商品不存在
            self.driver.find_element_by_id('com.zhongsu.online:id/et_search').click()
            self.driver.find_element_by_id('com.zhongsu.online:id/et_search').clear()
            self.driver.find_element_by_id('com.zhongsu.online:id/et_search').send_keys("text")
            self.driver.press_keycode(66)
            time.sleep(3)
            actual = self.driver.find_element_by_id('com.zhongsu.online:id/empty_msg_text').text
            self.assertEqual('空空如也', actual)
            # 模糊搜索
            self.driver.find_element_by_id('com.zhongsu.online:id/et_search').click()
            self.driver.find_element_by_id('com.zhongsu.online:id/et_search').clear()
            self.driver.find_element_by_id('com.zhongsu.online:id/et_search').send_keys("科思创")
            self.driver.press_keycode(66)
            time.sleep(3)
            actual = self.driver.find_element_by_id('com.zhongsu.online:id/tv_name').text
            self.assertIn('科思创', actual)
            # 筛选仓库
            self.driver.find_element_by_id('com.zhongsu.online:id/iv_filter').click()
            self.driver.implicitly_wait(20)
            self.driver.find_element_by_id('com.zhongsu.online:id/spinner_warehouse').click()
            self.driver.implicitly_wait(20)
            text = self.driver.find_elements_by_id('android:id/text1')[1].text
            if text == '浙江余姚':
                self.driver.find_element_by_xpath(
                    '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android'
                    '.widget.TextView[2]').click()
            self.driver.implicitly_wait(20)
            self.driver.find_element_by_id('com.zhongsu.online:id/tv_confirm').click()
            self.driver.implicitly_wait(20)
            actual = self.driver.find_elements_by_id('com.zhongsu.online:id/tv_area')[0].text
            self.assertEqual(text, actual)
            # 筛选供应状态
            self.driver.find_element_by_id('com.zhongsu.online:id/iv_filter').click()
            self.driver.implicitly_wait(20)
            self.driver.find_element_by_id('com.zhongsu.online:id/spinner_status').click()
            self.driver.implicitly_wait(20)
            self.driver.find_element_by_xpath(
                    "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android"
                    ".widget.TextView[3]").click()
            self.driver.implicitly_wait(20)
            self.driver.find_element_by_id('com.zhongsu.online:id/tv_confirm').click()
            self.driver.implicitly_wait(20)
            actual = self.driver.find_elements_by_id('com.zhongsu.online:id/btn_tag')[0].text
            self.assertIn('已下架', actual)
            # 筛选全部联系人
            self.driver.find_element_by_id('com.zhongsu.online:id/iv_filter').click()
            self.driver.implicitly_wait(20)
            self.driver.find_element_by_id('com.zhongsu.online:id/rl_contacts').click()
            time.sleep(3)
            text = self.driver.find_elements_by_id('android:id/text1')[2].text
            if text == '收到':
                self.driver.find_element_by_xpath(
                    '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android'
                    '.widget.TextView[3]').click()
            self.driver.implicitly_wait(20)
            self.driver.find_element_by_id('com.zhongsu.online:id/tv_confirm').click()
            self.driver.implicitly_wait(20)
            actual = self.driver.find_elements_by_id('com.zhongsu.online:id/tv_contacts')[0].text
            self.assertIn(text, actual)
            # 清除搜索框内容
            self.driver.find_element_by_id('com.zhongsu.online:id/et_search').click()
            self.driver.find_element_by_id('com.zhongsu.online:id/et_search').clear()
            time.sleep(3)
            Mouse_keyboard.click(self, x=970, y=2235)
            time.sleep(3)
        except Exception as _:
            f_name = sys._getframe().f_code.co_name  # 获取正在执行的函数名
            ScreenShot.getScreenShot(self, file="SalesManagementTest", case=f_name)

    # 编辑
    def test_04(self):
        try:
            self.driver.find_elements_by_id('com.zhongsu.online:id/ll_editor')[0].click()
            self.driver.implicitly_wait(20)
            text = self.driver.find_element_by_id('com.zhongsu.online:id/bar_title').text
            self.assertEqual('发布商品', text)
            self.driver.find_element_by_id('com.zhongsu.online:id/btn_next_to_business').click()
            self.driver.implicitly_wait(20)
            text = self.driver.find_element_by_id('com.zhongsu.online:id/tv_quoted_price_way').text
            if text == '基差报价':
                self.driver.find_element_by_id('com.zhongsu.online:id/tv_quoted_price_way').click()
                self.driver.implicitly_wait(20)
                self.driver.find_element_by_xpath('//android.widget.TextView[@text="现价"]').click()
                self.driver.implicitly_wait(20)
                self.driver.find_element_by_id('com.zhongsu.online:id/chk_select').click()
                self.driver.find_element_by_id('com.zhongsu.online:id/et_price').send_keys(random.randint(0, 10000))
                price = self.driver.find_element_by_id('com.zhongsu.online:id/et_price').text
                self.driver.find_element_by_id('com.zhongsu.online:id/btn_submit').click()
            else:
                self.driver.find_element_by_id('com.zhongsu.online:id/tv_quoted_price_way').click()
                self.driver.implicitly_wait(20)
                self.driver.find_element_by_xpath('//android.widget.TextView[@text="基差报价"]').click()
                self.driver.find_element_by_id('com.zhongsu.online:id/chk_select').click()
                self.driver.find_element_by_id(
                    'com.zhongsu.online:id/et_price_jicha').send_keys(random.randint(-2000, 10000))
                price = self.driver.find_element_by_id('com.zhongsu.online:id/et_price_jicha').text
                wait.slide(self, text='提交')
                self.driver.implicitly_wait(20)
                self.driver.find_element_by_id('com.zhongsu.online:id/btn_submit').click()
            self.driver.implicitly_wait(20)
            actual = self.driver.find_elements_by_id('com.zhongsu.online:id/tv_price')[0].text
            self.assertIn(price, actual)
        except Exception as _:
            f_name = sys._getframe().f_code.co_name  # 获取正在执行的函数名
            ScreenShot.getScreenShot(self, file="SalesManagementTest", case=f_name)

    # 上架和下架
    def test_05(self):
        try:
            self.driver.find_element_by_id('com.zhongsu.online:id/tv_standupdown').click()
            tv_name = self.driver.find_elements_by_id('com.zhongsu.online:id/tv_name')[0].text
            btn_tag = self.driver.find_elements_by_id('com.zhongsu.online:id/btn_tag')[0].text
            self.driver.find_elements_by_id('com.zhongsu.online:id/check_box')[0].click()
            if btn_tag == "上架中":
                self.driver.implicitly_wait(20)
                self.driver.find_element_by_id('com.zhongsu.online:id/tv_standdown').click()
                WebDriverWait(self.driver, 10, 0.5).until(lambda driver: driver.find_element_by_id(
                    'com.zhongsu.online:id/btn_tag'))
                btn_tag = self.driver.find_elements_by_id('com.zhongsu.online:id/btn_tag')[0].text
                self.assertEqual('已下架', btn_tag)
                self.driver.back()
                self.driver.implicitly_wait(20)
                user_nm = self.driver.find_element_by_id('com.zhongsu.online:id/tv_user_nm').text
                self.driver.find_elements_by_id('com.zhongsu.online:id/tab_image')[0].click()
                self.driver.implicitly_wait(20)
                self.driver.find_element_by_id('com.zhongsu.online:id/et_search').click()
                time.sleep(3)
                self.driver.find_element_by_id('com.zhongsu.online:id/et_search').send_keys(tv_name)
                time.sleep(3)
                Mouse_keyboard.click(self, x=986, y=2244)
                self.driver.implicitly_wait(20)
                company_count = self.driver.find_elements_by_id('com.zhongsu.online:id/tv_company')
                # 校验下架后不能查到这个商品
                i = 1
                while i <= len(company_count):
                    self.assertNotEqual(user_nm, company_count[len(company_count)-1].text)
                    i += 1
            else:
                self.driver.find_element_by_id('com.zhongsu.online:id/tv_standup').click()
                WebDriverWait(self.driver, 10, 0.5).until(lambda driver: driver.find_element_by_id(
                    'com.zhongsu.online:id/btn_tag'))
                btn_tag = self.driver.find_elements_by_id('com.zhongsu.online:id/btn_tag')[0].text
                self.assertEqual('上架中', btn_tag)
                self.driver.back()
                self.driver.implicitly_wait(20)
                user_nm = self.driver.find_element_by_id('com.zhongsu.online:id/tv_user_nm').text
                self.driver.find_elements_by_id('com.zhongsu.online:id/tab_image')[0].click()
                self.driver.implicitly_wait(20)
                self.driver.find_element_by_id('com.zhongsu.online:id/et_search').click()
                time.sleep(3)
                self.driver.find_element_by_id('com.zhongsu.online:id/et_search').send_keys(tv_name)
                time.sleep(3)
                Mouse_keyboard.click(self, x=986, y=2244)
                self.driver.implicitly_wait(20)
                company_name = self.driver.find_elements_by_id('com.zhongsu.online:id/tv_company')[0].text
                # 校验上架后能查到这个商品
                self.assertEqual(user_nm, company_name)
            self.driver.back()
            self.driver.back()
            self.driver.back()
            self.driver.implicitly_wait(20)
            self.driver.find_element_by_xpath('//android.widget.TextView[@text="我的"]').click()
            time.sleep(3)
            self.driver.find_element_by_id('com.zhongsu.online:id/btn_my_supply').click()
        except Exception as _:
            f_name = sys._getframe().f_code.co_name  # 获取正在执行的函数名
            ScreenShot.getScreenShot(self, file="SalesManagementTest", case=f_name)

    # 上架的商品点击上架，下架的商品点击下架
    def test_06(self):
        try:
            self.driver.implicitly_wait(20)
            self.driver.find_element_by_id('com.zhongsu.online:id/tv_standupdown').click()
            btn_tag = self.driver.find_elements_by_id('com.zhongsu.online:id/btn_tag')[0].text
            self.driver.find_elements_by_id('com.zhongsu.online:id/check_box')[0].click()
            if btn_tag == "上架中":
                self.driver.implicitly_wait(20)
                self.driver.find_element_by_id('com.zhongsu.online:id/tv_standup').click()
                self.assertEqual('你选的商品都处于上架状态，无需重复上架！', toast.get_toast_text(self, toast='你选的商品都处于上架状态，无需重复上架'))
            else:
                self.driver.implicitly_wait(20)
                self.driver.find_element_by_id('com.zhongsu.online:id/tv_standdown').click()
                self.assertEqual('你选的商品都处于下架状态，无需重复下架！', toast.get_toast_text(self, toast='你选的商品都处于下架状态，无需重复下架'))
            self.driver.find_element_by_id('com.zhongsu.online:id/ib_back_layout_toolbar_back_righttv').click()
        except Exception as _:
            f_name = sys._getframe().f_code.co_name  # 获取正在执行的函数名
            ScreenShot.getScreenShot(self, file="SalesManagementTest", case=f_name)

    # 测试快速发布
    def test_07(self):
        try:
            for i in range(1):
                self.driver.implicitly_wait(20)
                self.driver.find_element_by_id('com.zhongsu.online:id/tv_publish').click()
                self.driver.implicitly_wait(20)
                self.driver.find_element_by_id('com.zhongsu.online:id/q_product_sel').click()
                self.driver.implicitly_wait(20)
                self.driver.find_element_by_id('com.zhongsu.online:id/et_search').click()
                self.driver.find_element_by_id('com.zhongsu.online:id/et_search').send_keys('tpe')
                time.sleep(3)
                Mouse_keyboard.click(self, x=978, y=2241)
                self.driver.implicitly_wait(20)
                self.driver.find_elements_by_id('com.zhongsu.online:id/chk_select')[0].click()
                self.driver.find_element_by_id('com.zhongsu.online:id/btn_confirm').click()
                self.driver.implicitly_wait(20)
                self.driver.find_element_by_id('com.zhongsu.online:id/q_price').send_keys(10000)
                self.driver.find_element_by_id('com.zhongsu.online:id/q_supplies').send_keys(10000)
                self.driver.find_element_by_id('com.zhongsu.online:id/q_publish').click()
                if i == 0:
                    self.assertEqual('发布成功', toast.get_toast_text(self, toast='发布成功'))
                    self.driver.implicitly_wait(20)
                    name = self.driver.find_elements_by_id('com.zhongsu.online:id/tv_name')[0].text
                else:
                    self.assertIn('商品"%s"已经存在,请勿重复发布!' % name, toast.get_toast_text(
                        self, toast='商品"%s"已经存在,请勿重复发布!' % name))
                    self.driver.back()
                # 删除
                self.driver.implicitly_wait(20)
                self.driver.find_elements_by_id('com.zhongsu.online:id/ll_del')[0].click()
                self.driver.implicitly_wait(20)
                self.driver.find_element_by_id('com.zhongsu.online:id/now_approve_tv').click()
                self.driver.implicitly_wait(20)
                actual = self.driver.find_elements_by_id('com.zhongsu.online:id/tv_name')[0].text
                self.assertNotEqual(name, actual)
        except Exception as _:
            f_name = sys._getframe().f_code.co_name  # 获取正在执行的函数名
            ScreenShot.getScreenShot(self, file="SalesManagementTest", case=f_name)

    # 测试快速发布
    def test_08(self):
        try:
            self.driver.find_element_by_id('com.zhongsu.online:id/tv_update').click()
            title = self.driver.find_element_by_id(
                'com.zhongsu.online:id/toolbar_title_layout_toolbar_back_righttv').text
            self.assertEqual('我的供应', title)
        except Exception as _:
            f_name = sys._getframe().f_code.co_name
            ScreenShot.getScreenShot(self, file='SalesManagementTest', case=f_name)
