import paramunittest
import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import PARM
from selenium.webdriver.common.keys import Keys


class AuthenticationReportTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        url = "https://shop.21cp.work/authentication/256062966372380672.html"
        cls.driver.get(url)
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    # 验证滚动图片是否滚动到第三张
    def test_01(self):
        self.driver.refresh()
        time.sleep(12)
        result = self.driver.find_element_by_xpath('//*[@id="swiper"]/div/div[4]').get_attribute('class')
        self.assertIn('swiper-slide-visible swiper-slide-active', result)
        src = self.driver.find_element_by_xpath('//*[@id="swiper"]/div/div[4]/img').get_attribute('src')
        result = src.split('?')[0]  # 截取问号之前的首个字符串
        src1 = self.driver.find_element_by_xpath('/html/body/div[5]/div/div[4]/div/div[3]/div[1]/img').get_attribute('src')
        expect = src1.split('?')[0]
        self.assertEqual(expect, result)

    # 验证视频播放成功
    def test_02(self):
        self.driver.refresh()
        i = 1
        while i <= 6:
            self.driver.find_element_by_class_name('swiper-icon-next').click()
            time.sleep(1)
            i += 1
        self.driver.find_element_by_class_name('swiper-icon-prev').click()
        result = self.driver.find_element_by_xpath('//*[@id="swiper"]/div/div[7]/img[2]').get_attribute('video')
        self.assertEqual(
            'https://zs-test-image.21cp.work/zsAuthentication/video/48642459907e4f6b90c41df6bf6d1c2f.mp4', result)
        result = self.driver.find_element_by_xpath('//*[@id="swiper"]/div/div[7]').get_attribute('class')
        self.assertIn('swiper-slide-visible swiper-slide-active', result)
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_xpath('//*[@id="swiper"]/div/div[7]/img[2]').click()
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_xpath('/html/body/div[3]/div/i').click()

    # 验证报告名称正确
    def test_03(self):
        result = self.driver.find_element_by_xpath('/html/body/div[6]/div').text
        lis = []
        for expect in PARM.report_info:
            for actual in result.split(' '):
                if expect == actual:
                    lis.append(actual)
        self.assertEqual(expect, actual)
        self.assertEqual(4, len(lis))

    # 右侧导航栏点击
    def test_04(self):
        # 点击申请认证
        self.driver.find_element_by_xpath('/html/body/div[7]/div[1]').click()
        h = self.driver.current_window_handle
        handles = self.driver.window_handles
        for windows in handles:
            self.driver.switch_to.window(windows)
            if self.driver.title == '申请认证-中塑在线企业认证':
                break
        self.assertEqual(self.driver.title, '申请认证-中塑在线企业认证')
        target = self.driver.find_element_by_xpath('//*[@id="customer"]/div[2]/div')
        self.driver.execute_script("arguments[0].scrollIntoView();", target)
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_xpath('//*[@id="customer"]/div[2]/div/a').click()
        self.driver.close()
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[-1])
        self.driver.implicitly_wait(20)
        result = self.driver.find_element_by_xpath('//*[@id="isAuthentication"]').get_attribute('class')
        self.assertIn('checked', result)
        self.driver.find_element_by_xpath('/html/body/div[5]/div[4]/div[1]/div[2]/div[2]/div[1]/div[3]/a[2]/i').click()
        self.driver.close()
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[-1])
        self.driver.close()
        self.driver.switch_to.window(h)
        # 点击在线客服
        self.driver.switch_to.window(h)
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_xpath('/html/body/div[7]/div[2]').click()
        time.sleep(3)  # div弹窗有可能隐式等待无用需要强制等待
        result = self.driver.find_element_by_class_name('layui-layer-title').text
        self.assertEqual('中塑在线客服', result)
        self.driver.find_element_by_xpath('//*[@id="layui-layer1"]/span[1]/a').click()
        # 未登录点击匿名投诉
        self.driver.find_element_by_id('j-open-ticket').click()
        time.sleep(3)
        result = self.driver.find_element_by_class_name('layui-layer-content').text
        self.assertEqual('您还未登陆，请登录后提交意见反馈信息！', result)
        self.driver.refresh()
        # 点击扫码分享
        move = self.driver.find_element_by_xpath('/html/body/div[7]/div[4]')
        ActionChains(self.driver).move_to_element(move).perform()
        self.driver.implicitly_wait(20)
        result = self.driver.find_element_by_xpath('/html/body/div[7]/div[4]/div[2]/div[2]').text
        self.assertEqual('手机扫码分享', result)

    # 验证企业工商信息--查看更多按钮
    def test_05(self):
        target = self.driver.find_element_by_xpath('/html/body/div[10]/div[3]/div/ul/li[11]/div[2]')
        self.driver.execute_script("arguments[0].scrollIntoView();", target)  # 滚动条拖动到可见的元素去
        time.sleep(2)
        expect = self.driver.find_element_by_xpath('/html/body/div[10]/div[3]/div/ul/li[11]/div[2]').get_attribute('content')
        self.driver.find_element_by_class_name('look-over').click()
        time.sleep(2)
        result = self.driver.find_element_by_xpath('//*[@id="scroll-content"]').text
        self.assertEqual(expect, result)
        self.driver.find_element_by_xpath('/html/body/div[10]/div[3]/div/div[1]/div/header/i').click()

    # 点击在线洽谈
    def test_06(self):
        target = self.driver.find_element_by_xpath('/html/body/div[10]/div[7]/div')
        self.driver.execute_script("arguments[0].scrollIntoView();", target)
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_xpath('/html/body/div[10]/div[7]/div/div[1]/div[4]/a').click()
        time.sleep(2)
        h = self.driver.current_window_handle
        handles = self.driver.window_handles
        for windows in handles:
            self.driver.switch_to.window(windows)
            if self.driver.title == '账号登录-中塑在线-21世纪塑料行业门户':
                break
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_name('username').send_keys('kaiyu12')
        self.driver.find_element_by_name('password').send_keys(123456)
        self.driver.find_element_by_xpath('//*[@id="login"]/input[4]').click()
        self.driver.implicitly_wait(20)
        result = self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/div[1]/div[1]/strong').text
        self.assertEqual('测试一笑有限公司', result)
        self.driver.close()
        self.driver.switch_to.window(h)

    # 点击查看供应
    def test_07(self):
        self.driver.refresh()
        expect = self.driver.find_element_by_class_name('company-name').text
        target = self.driver.find_element_by_xpath('/html/body/div[10]/div[8]/h1')
        self.driver.execute_script("arguments[0].scrollIntoView();", target)
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_xpath('/html/body/div[10]/div[8]/div[2]/div/a').click()
        h = self.driver.current_window_handle
        handles = self.driver.window_handles
        for windows in handles:
            self.driver.switch_to.window(windows)
            if self.driver.title == '企业产品-中塑在线商铺-中塑在线塑料行业门户':
                break
        self.driver.implicitly_wait(20)
        result = self.driver.find_element_by_class_name('company-name').text
        self.driver.close()
        self.driver.switch_to.window(h)
        self.assertEqual(expect, result)

    # 导航栏页面定位
    def test_08(self):
        # 点击顶部认证信息
        self.driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div[2]').click()
        i = 1
        while i <= 60:
            try:
                result = self.driver.find_element_by_xpath('/html/body/div[10]/div[1]/div[2]').get_attribute('class')
                self.assertIn('active', result)
                break
            except Exception as error:
                print(i, error)
                time.sleep(1)
                i += 1
        # 点击顶部中塑实力
        self.driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div[3]').click()
        i = 1
        while i <= 60:
            try:
                result = self.driver.find_element_by_xpath('/html/body/div[10]/div[1]/div[6]').get_attribute('class')
                self.assertIn('active', result)
                break
            except Exception as error:
                print(i, error)
                time.sleep(1)
                i += 1
        # 点击导航返回顶部按钮
        self.driver.find_element_by_xpath('/html/body/div[10]/div[1]/div[7]').click()
        i = 1
        while i <= 60:
            try:
                result = self.driver.find_element_by_xpath('/html/body/div[10]/div[1]/div[1]').get_attribute('class')
                self.assertIn('active', result)
                result = self.driver.find_element_by_xpath('/html/body/div[10]/div[2]/h1')
                self.assertTrue(result)
                break
            except Exception as error:
                print(i, error)
                time.sleep(1)
                i += 1

    # 点击顶部导航栏公司名称跳转商铺
    def test_09(self):
        expect = self.driver.find_element_by_class_name('company-name').text
        self.driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/a').click()
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[-1])
        self.driver.implicitly_wait(20)
        company = self.driver.find_element_by_class_name('company-name').text
        self.assertEqual(expect, company)
        # 点击商铺顶部导航栏中塑认证跳转报告
        result = self.driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/a[7]').text
        self.assertEqual('中塑认证', result)
        self.driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/a[7]').click()
        i = 1
        while i <= 60:
            try:
                self.assertIn('%s全景展示' % company, self.driver.title)
                break
            except Exception as error:
                print(i, error)
                i += 1
        # 点击商铺中塑认证勋章跳转报告
        self.driver.implicitly_wait(20)
        i = 1
        while i <= 60:
            try:
                self.driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/a').click()
                break
            except Exception as error:
                print(i, error)
                i += 1
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[-1])
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[2]/div[1]/a').click()
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[-1])
        self.assertIn('%s全景展示' % company, self.driver.title)

if __name__ == '__main__':
    unittest.main()
