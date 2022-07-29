import APP_pre
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


class SearchTest(APP_pre.LoginTest):
    # 搜供应
    def test_01(self):
        # 切换搜索产品类型成功
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_xpath('//*[@resource-id="com.zhongsu.online:id/tab_layout"]/android.widget'
                                          '.LinearLayout/android.widget.LinearLayout[1]').click()
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_id('com.zhongsu.online:id/et_search').click()
        self.driver.implicitly_wait(20)
        hot = self.driver.find_element_by_id('com.zhongsu.online:id/tv_hot_goods').text
        self.assertEqual('热门原料推荐', hot)
        self.driver.find_element_by_id('com.zhongsu.online:id/tv_goods').click()
        self.driver.find_element_by_xpath('/hierarchy/android.view.ViewGroup/android.widget.FrameLayout[2]'
                                          '/android.widget.FrameLayout/android.widget.RelativeLayout'
                                          '/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView'
                                          '/android.widget.RelativeLayout[4]/android.widget.TextView').click()
        self.driver.implicitly_wait(20)
        hot = self.driver.find_element_by_id('com.zhongsu.online:id/tv_hot_goods').text
        self.assertEqual('热门助剂推荐', hot)
        # 跳转搜索页面
        self.driver.find_element_by_id('com.zhongsu.online:id/et_search').click()
        time.sleep(3)
        self.driver.find_element_by_id('com.zhongsu.online:id/et_search').send_keys('神高达上东国际阿萨德刚回家是大概就爱上大公鸡')
        actions = ActionChains(self.driver)
        actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        actions.w3c_actions.pointer_action.move_to_location(986, 2244)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.pause(0.1)
        actions.w3c_actions.pointer_action.release()
        actions.perform()
        self.driver.implicitly_wait(20)
        result = self.driver.find_element_by_id('com.zhongsu.online:id/tv_').text
        self.assertEqual('太不可思议了！竟无人供应', result)
        self.driver.find_element_by_id('com.zhongsu.online:id/iv_back').click()
        # 正常显示历史标签，点击标签搜索
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout'
                                          '/android.widget.FrameLayout/android.widget.LinearLayout'
                                          '/android.widget.FrameLayout/android.view.ViewGroup'
                                          '/androidx.viewpager.widget.ViewPager/android.widget.LinearLayout'
                                          '/android.widget.ScrollView/android.widget.LinearLayout'
                                          '/android.widget.LinearLayout[1]/android.widget.LinearLayout'
                                          '/android.view.ViewGroup[2]/android.widget.TextView[1]').click()
        self.driver.implicitly_wait(20)
        result = self.driver.find_element_by_id('com.zhongsu.online:id/et_search').text
        self.assertEqual('神高达上东国际阿萨德刚回家是大概就爱上大公鸡', result)
        self.driver.find_element_by_id('com.zhongsu.online:id/iv_back').click()
        # 点击热门精选跳转商品详情
        self.driver.implicitly_wait(20)
        element = self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout'
                                                    '/android.widget.FrameLayout/android.widget.LinearLayout'
                                                    '/android.widget.FrameLayout/android.view.ViewGroup'
                                                    '/androidx.viewpager.widget.ViewPager/android.widget.LinearLayout'
                                                    '/android.widget.ScrollView/android.widget.LinearLayout'
                                                    '/android.widget.RelativeLayout'
                                                    '/androidx.recyclerview.widget.RecyclerView'
                                                    '/android.widget.LinearLayout[1]/android.view.ViewGroup'
                                                    '/android.widget.TextView[1]')
        expect = element.text
        element.click()
        self.driver.implicitly_wait(20)
        result = self.driver.find_element_by_id('com.zhongsu.online:id/tv_name').text
        self.assertEqual(expect, result)
        self.driver.find_element_by_id('com.zhongsu.online:id/img_back').click()
        # 点击大家都在搜标签跳转页面
        self.driver.implicitly_wait(20)
        el = self.driver.find_element_by_id('com.zhongsu.online:id/tv_goods').text
        el1 = self.driver.find_element_by_xpath(
            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout'
            '/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup'
            '/androidx.viewpager.widget.ViewPager/android.widget.LinearLayout/android.widget.ScrollView'
            '/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout'
            '/android.view.ViewGroup[2]/android.widget.TextView[1]')
        expect = el1.text
        el1.click()
        WebDriverWait(self.driver, 20, 0.01).until(
            EC.presence_of_element_located((By.ID, 'com.zhongsu.online:id/et_search')))
        result = self.driver.find_element_by_id('com.zhongsu.online:id/et_search').text
        self.assertEqual(expect, result)
        el2 = self.driver.find_element_by_xpath(
            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout'
            '/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup'
            '/android.widget.LinearLayout/android.widget.HorizontalScrollView/android.widget.LinearLayout'
            '/android.widget.LinearLayout[1]/android.widget.RelativeLayout/android.widget.TextView')
        result = el2.text
        self.assertEqual(el, result)
        self.driver.find_element_by_id('com.zhongsu.online:id/iv_back').click()

    # 搜索咨询
    def test_02(self):
        # 点击热门咨询推荐进入详情
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_id('com.zhongsu.online:id/info_title').click()
        self.driver.implicitly_wait(20)
        el = self.driver.find_element_by_xpath(
            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout'
            '/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup'
            '/androidx.viewpager.widget.ViewPager/android.widget.LinearLayout/android.widget.ScrollView'
            '/android.widget.LinearLayout/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView'
            '/android.widget.LinearLayout[1]/android.view.ViewGroup/android.widget.LinearLayout[1]'
            '/android.widget.TextView[1]')
        expect = el.text
        el.click()
        self.driver.implicitly_wait(20)
        el1 = self.driver.find_element_by_xpath(
            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout'
            '/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout'
            '/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout'
            '/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View'
            '/android.view.View[1]')
        self.assertEqual(expect, el1.text)
        self.driver.find_element_by_id('com.zhongsu.online:id/btn_back').click()
        # 点击大家都在搜的标签
        self.driver.implicitly_wait(20)
        el = self.driver.find_element_by_xpath(
            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout'
            '/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup'
            '/androidx.viewpager.widget.ViewPager/android.widget.LinearLayout/android.widget.ScrollView'
            '/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout'
            '/android.view.ViewGroup[2]/android.widget.TextView[1]')
        expect = el.text
        el.click()
        WebDriverWait(self.driver, 20, 0.01).until(
            EC.presence_of_element_located((By.ID, 'com.zhongsu.online:id/et_search')))
        el1 = self.driver.find_element_by_id('com.zhongsu.online:id/et_search')
        self.assertEqual(expect, el1.text)
        self.driver.back()

    # 搜索物性
    def test_03(self):
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_id('com.zhongsu.online:id/pd_title').click()
        # 搜索热门产品推荐
        self.driver.find_element_by_id('com.zhongsu.online:id/et_search').clear()
        self.driver.implicitly_wait(20)
        el = self.driver.find_element_by_xpath(
            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout'
            '/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup'
            '/androidx.viewpager.widget.ViewPager/android.widget.LinearLayout/android.widget.ScrollView'
            '/android.widget.LinearLayout/android.widget.RelativeLayout/android.view.ViewGroup'
            '/android.widget.FrameLayout[1]/android.widget.LinearLayout')
        expect = el.text
        print(expect)
        el.click()
        self.driver.implicitly_wait(20)
        self.assertTrue(self.driver.find_element_by_xpath('//*[@text="%s"]' % expect))
        self.driver.back()
        # 点击大家都在搜的标签
        self.driver.implicitly_wait(20)
        el = self.driver.find_element_by_xpath(
            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout'
            '/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup'
            '/androidx.viewpager.widget.ViewPager/android.widget.LinearLayout/android.widget.ScrollView'
            '/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout'
            '/android.view.ViewGroup[2]/android.widget.TextView[1]')
        expect = el.text
        el.click()
        WebDriverWait(self.driver, 20, 0.01).until(
            EC.presence_of_element_located((By.ID, 'com.zhongsu.online:id/et_search')))
        el1 = self.driver.find_element_by_id('com.zhongsu.online:id/et_search')
        self.assertEqual(expect, el1.text)
        self.driver.back()

    # 搜索企业
    def test_04(self):
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_id('com.zhongsu.online:id/corp_title').click()
        # 搜索热门企业推荐进入详情
        el = self.driver.find_element_by_xpath(
            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout'
            '/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup'
            '/androidx.viewpager.widget.ViewPager/android.widget.LinearLayout/android.widget.ScrollView'
            '/android.widget.LinearLayout/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView'
            '/android.widget.LinearLayout[1]/android.view.ViewGroup/android.widget.TextView[1]')
        expect = el.text
        el.click()
        self.driver.implicitly_wait(20)
        result = self.driver.find_element_by_id('com.zhongsu.online:id/bar_title').text
        self.assertEqual(expect, result)
        self.driver.back()
        self.driver.implicitly_wait(20)
        # 点击大家都在搜的标签
        self.driver.implicitly_wait(20)
        el = self.driver.find_element_by_xpath(
            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout'
            '/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup'
            '/androidx.viewpager.widget.ViewPager/android.widget.LinearLayout/android.widget.ScrollView'
            '/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout'
            '/android.view.ViewGroup[2]/android.widget.TextView[1]')
        expect = el.text
        el.click()
        WebDriverWait(self.driver, 20, 0.01).until(
            EC.presence_of_element_located((By.ID, 'com.zhongsu.online:id/et_search')))
        el1 = self.driver.find_element_by_id('com.zhongsu.online:id/et_search')
        self.assertEqual(expect, el1.text)
        self.driver.back()





















