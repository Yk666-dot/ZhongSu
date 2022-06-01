from apptest_Android import APP_pre
from Script import toast
import time
from Script import wait


class MyShopTest(APP_pre.LoginTest):
    # 未登录点击我的商铺,跳转登录
    def test_01(self):
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_xpath(
            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout'
            '/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout'
            '/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.widget.LinearLayout[5]'
            '/android.widget.LinearLayout/android.widget.ImageView').click()
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_id('com.zhongsu.online:id/btn_my_shop').click()
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

    # 有权限账号进入商铺
    def test_02(self):
        self.driver.implicitly_wait(20)
        expect = self.driver.find_element_by_id('com.zhongsu.online:id/tv_user_nm').text
        self.driver.find_element_by_id('com.zhongsu.online:id/btn_my_shop').click()
        self.driver.implicitly_wait(20)
        result = self.driver.find_element_by_xpath(
            '//*[@resource-id="app"]/android.view.View[1]/android.view.View[1]').text
        self.assertEqual(expect, result)  # 校验店铺名字
        # 点击分享
        self.driver.find_element_by_id('com.zhongsu.online:id/btn_share').click()
        self.driver.implicitly_wait(20)
        share = self.driver.find_element_by_id('com.zhongsu.online:id/tv_title').text
        self.assertEqual('分享', share)
        self.driver.back()

    # 测试首页功能
    def test_03(self):
        # 跳转商品详情
        self.driver.implicitly_wait(20)
        name = self.driver.find_element_by_xpath(
            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android'
            '.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.webkit.WebView'
            '/android.webkit.WebView/android.view.View/android.view.View/android.view.View[8]/android.view.View[2]')
        expect = name.text
        name.click()
        self.driver.implicitly_wait(20)
        result = self.driver.find_element_by_id('com.zhongsu.online:id/tv_name').text
        self.assertEqual(expect, result)  # 验证跳转的详情页正确
        self.driver.back()
        # 点击工商信息
        self.driver.find_element_by_xpath(
            '//android.widget.TabWidget/android.view.View[2]/android.view.View[1]').click()
        time.sleep(3)
        result = self.driver.find_element_by_xpath(
            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android'
            '.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.webkit.WebView'
            '/android.webkit.WebView/android.view.View/android.view.View/android.view.View[22]/android.view.View['
            '2]/android.view.View/android.view.View/android.view.View/android.view.View[1]').text
        self.assertEqual('法人代表:', result)
        #  点击企业资质
        self.driver.find_element_by_xpath(
            '//android.widget.TabWidget/android.view.View[3]/android.view.View[1]').click()
        self.driver.implicitly_wait(20)
        result = self.driver.find_element_by_xpath(
            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android'
            '.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.webkit.WebView'
            '/android.webkit.WebView/android.view.View/android.view.View/android.view.View[22]/android.view.View['
            '2]/android.view.View/android.view.View/android.view.View/android.view.View[1]').text
        self.assertIn('资质证书', result)
        # 点击授权认证
        self.driver.find_element_by_xpath(
            '//android.widget.TabWidget/android.view.View[4]/android.view.View[1]').click()
        time.sleep(3)
        result = self.driver.find_element_by_xpath(
            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android'
            '.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.webkit.WebView'
            '/android.webkit.WebView/android.view.View/android.view.View/android.view.View[22]/android.view.View['
            '2]/android.view.View/android.view.View/android.view.View/android.view.View[1]').text
        self.assertIn('管理员授权委托书', result)
        # 点击商品图册查看更多
        wait.slide(self, text="查看更多").click
        self.driver.find_element_by_xpath(
            '//*[@resource-id="app"]/android.view.View[1]/android.view.View[24]/android.view.View[1]').click()
        self.driver.implicitly_wait(20)
        result = self.driver.find_element_by_xpath(
            '//*[@resource-id="app"]/android.view.View[1]/android.view.View[2]/android.view.View[2]').text
        self.assertEqual('供应商品', result)
        # 点击收藏
        self.driver.find_element_by_xpath('//*[@text="首页"]').click()
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android'
                                          '.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout'
                                          '/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView'
                                          '/android.view.View/android.view.View/android.view.View['
                                          '23]/android.view.View[1]').click()
        self.assertEqual('收藏成功', toast.get_toast_text(self, toast='收藏成功'))
        time.sleep(2)
        self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android'
                                          '.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout'
                                          '/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView'
                                          '/android.view.View/android.view.View/android.view.View['
                                          '23]/android.view.View[1]').click()
        self.assertEqual("已取消收藏", toast.get_toast_text(self, toast="已取消收藏"))
        time.sleep(2)
        # 点击联机洽谈
        self.driver.find_element_by_xpath(
            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android'
            '.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.webkit.WebView'
            '/android.webkit.WebView/android.view.View/android.view.View/android.view.View[23]'
            '/android.view.View[3]').click()
        self.assertEqual("无法与自己建立会话", toast.get_toast_text(self, toast="无法与自己建立会话"))

    # 进入供应列表
    def test_04(self):
        self.driver.find_element_by_xpath('//*[@resource-id="app"]/android.view.View/android.view.View[4]').click()
        self.driver.implicitly_wait(20)
        # 跳转商品详情
        self.driver.find_element_by_xpath(
            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android'
            '.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.webkit.WebView'
            '/android.webkit.WebView/android.view.View/android.view.View/android.view.View[6]/android.view.View['
            '1]/android.view.View[2]').click()
        self.driver.implicitly_wait(20)
        expect = self.driver.find_element_by_xpath(
            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android'
            '.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.webkit.WebView'
            '/android.webkit.WebView/android.view.View/android.view.View/android.view.View[6]/android.view.View['
            '2]/android.view.View[3]/android.view.View[1]/android.view.View[1]').text
        self.driver.find_element_by_xpath(
            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android'
            '.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.webkit.WebView'
            '/android.webkit.WebView/android.view.View/android.view.View/android.view.View[6]/android.view.View['
            '2]/android.view.View[3]/android.view.View[1]/android.view.View[1]').click()
        self.driver.implicitly_wait(20)
        actual = self.driver.find_element_by_id('com.zhongsu.online:id/tv_name').text
        self.assertIn(actual, expect)
        self.driver.back()
        self.driver.implicitly_wait(20)
        try:
            expect = self.driver.find_element_by_xpath(
                '//*[@resource-id="productList"]/android.view.View[1]/android.view.View[4]').text
            self.driver.find_element_by_xpath(
                '//*[@resource-id="app"]/android.view.View[1]/android.view.View[6]/android.view.View['
                '2]/android.view.View[2]').click()
            actual = self.driver.find_element_by_xpath('//*[@resource-id="productList"]/android.view.View[1]').text
            self.assertIn(expect, actual)
        except Exception as error:
            print(error)
            self.driver.find_element_by_xpath(
                '//*[@resource-id="app"]/android.view.View[1]/android.view.View[6]/android.view.View['
                '2]/android.view.View[2]').click()
        # 切换商品类型
        self.driver.find_element_by_xpath(
            '//*[@resource-id="app"]/android.view.View/android.view.View[5]/android.view.View[2]').click()
        # 进入关于我们
        self.driver.find_element_by_xpath(
            '//*[@resource-id="app"]/android.view.View/android.view.View[3]').click()
        # 进入联系我们
        wait.ExplicitWait(self, element='//*[@resource-id="app"]/android.view.View/android.view.View[4]')
        self.driver.find_element_by_xpath('//*[@resource-id="app"]/android.view.View/android.view.View[4]').click()
        self.driver.implicitly_wait(20)
        # 点击洽谈
        self.driver.find_element_by_xpath(
            '//*[@resource-id="app"]/android.view.View/android.view.View[5]/android.view.View[3]').click()
        time.sleep(1)
        self.assertEqual("无法与自己建立会话", toast.get_toast_text(self, toast="无法与自己建立会话"))
        # 点击导航
        self.driver.find_element_by_xpath(
            '//*[@resource-id="app"]/android.view.View/android.view.View[5]/android.view.View[2]').click()
        self.driver.implicitly_wait(20)
        expect = self.driver.find_element_by_id('com.zhongsu.online:id/baidu_btn').text
        self.assertIn('百度地图', expect)

