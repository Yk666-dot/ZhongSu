import APP_pre
from Script import toast
import time
from selenium.webdriver.support.ui import WebDriverWait #注意区分大小写，导入WebDriverWait等待的类
from selenium.webdriver.support import expected_conditions as EC #es,expected_conditions首字母，方便调用方法。as取一个别名，调方法的话直接EC.
from selenium.webdriver.common.by import By
import random


class RndPassword:
    def password(self):
        i = 1
        lis = []
        while i <= 6:
            lis.append(str(random.randint(0, 9)))
            i += 1
        return ''.join(lis)


class LoginTest(APP_pre.LoginTest):

    # 手机号验证码错误提示
    def test01(self):
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_xpath(
            '//*[@resource-id="com.zhongsu.online:id/tab_layout"]/android.widget.LinearLayout[1]'
            '/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.ImageView[1]').click()
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_xpath('//*[@resource-id="com.zhongsu.online:id/btn_login"]').click()
        self.driver.find_element_by_xpath('//*[@resource-id="com.zhongsu.online:id/et_user_account"]').send_keys('18888648053')
        self.driver.find_element_by_xpath('//*[@resource-id="com.zhongsu.online:id/btn_submit_login"]').click()
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_xpath('//*[@resource-id="com.zhongsu.online:id/now_approve_tv"]').click()

        self.driver.implicitly_wait(20)
        self.driver.keyevent(8)
        self.driver.keyevent(9)
        self.driver.keyevent(10)
        self.driver.keyevent(11)
        self.driver.keyevent(12)
        self.driver.keyevent(13)
        self.assertEqual('验证码错误', toast.get_toast_text(self, toast='验证码错误'))

    # 手机号验证码登录成功
    def test02(self):
        self.driver.find_element_by_xpath('//*[@resource-id="com.zhongsu.online:id/img_finish"]').click()
        self.driver.find_element_by_xpath('//*[@resource-id="com.zhongsu.online:id/btn_submit_login"]').click()
        i = 1
        while i <= 6:
            self.driver.keyevent(13)
            i += 1
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout'
                                          '/android.widget.FrameLayout/android.widget.LinearLayout'
                                          '/android.widget.FrameLayout/android.widget.RelativeLayout'
                                          '/android.widget.HorizontalScrollView/android.widget.LinearLayout'
                                          '/android.widget.LinearLayout[5]/android.widget.LinearLayout'
                                          '/android.widget.ImageView').click()
        self.driver.implicitly_wait(20)
        result = self.driver.find_element_by_id('com.zhongsu.online:id/tv_account_name').text
        self.assertEqual("kaiyu12", result)
        self.driver.find_element_by_id('com.zhongsu.online:id/im_setting').click()
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_id('com.zhongsu.online:id/tv_cancel').click()
        self.driver.find_element_by_id('com.zhongsu.online:id/now_approve_tv').click()

    # 账号密码登录
    def test03(self):
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_xpath('//*[@resource-id="com.zhongsu.online:id/btn_login"]').click()
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_xpath(
            '//*[@resource-id="com.zhongsu.online:id/lin_password"]/android.widget.ImageView[1]').click()
        time.sleep(3)
        self.driver.find_element_by_id('com.zhongsu.online:id/et_user_account').click()
        result = self.driver.find_element_by_id('com.zhongsu.online:id/et_user_account').text
        self.assertEqual('18888648053', result)
        self.driver.find_element_by_id('com.zhongsu.online:id/et_user_password').send_keys('123456')
        self.driver.find_element_by_id('com.zhongsu.online:id/chk_protocol').click()
        self.driver.find_element_by_id('com.zhongsu.online:id/rel_submit_login').click()
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_xpath('//*[@resource-id="com.zhongsu.online:id/tab_layout"]'
                                          '/android.widget.LinearLayout[1]/android.widget.LinearLayout[5]'
                                          '/android.widget.LinearLayout[1]/android.widget.ImageView[1]').click()
        self.driver.implicitly_wait(20)
        result = self.driver.find_element_by_id('com.zhongsu.online:id/tv_account_name').text
        self.assertEqual("kaiyu12", result)
        self.driver.find_element_by_id('com.zhongsu.online:id/im_setting').click()
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_id('com.zhongsu.online:id/tv_cancel').click()
        self.driver.find_element_by_id('com.zhongsu.online:id/now_approve_tv').click()

        # 账号输入信息不正确，登录失败
    def test04(self):
        # 密码错误
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_xpath('//*[@resource-id="com.zhongsu.online:id/btn_login"]').click()
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_id('com.zhongsu.online:id/chk_protocol').click()
        self.driver.find_element_by_id('com.zhongsu.online:id/et_user_password').send_keys('12345')
        self.driver.find_element_by_id('com.zhongsu.online:id/rel_submit_login').click()
        self.driver.implicitly_wait(20)
        tip = self.driver.find_element_by_id('com.zhongsu.online:id/hint_content_tv').text
        self.assertEqual('请输入正确的密码', tip)
        self.driver.find_element_by_id('com.zhongsu.online:id/now_approve_tv').click()
        self.driver.implicitly_wait(20)
        # 账号未注册
        self.driver.find_element_by_id('com.zhongsu.online:id/et_user_account').clear()
        self.driver.find_element_by_id('com.zhongsu.online:id/et_user_account').send_keys(12366662)
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_id('com.zhongsu.online:id/rel_submit_login').click()
        self.driver.implicitly_wait(20)
        tip = self.driver.find_element_by_id('com.zhongsu.online:id/hint_content_tv').text
        self.assertEqual('账号错误或尚未注册，请核对账号或使用验证码注册并登录', tip)
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_id('com.zhongsu.online:id/last_approve_tv').click()

    # 打开使用协议
    def test05(self):
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_id('com.zhongsu.online:id/btn_protocol').click()
        self.driver.implicitly_wait(20)
        result = self.driver.find_element_by_id('com.zhongsu.online:id/toolbar_title_layout_toolbar_back_righttv').text
        self.assertEqual('平台协议', result)
        self.driver.find_element_by_id('com.zhongsu.online:id/ib_back_layout_toolbar_back_righttv').click()

    # 忘记密码
    def test06(self):
        # 手机号错误
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_id('com.zhongsu.online:id/tv_forget').click()
        WebDriverWait(self.driver, 20, 0.5).until(EC.presence_of_element_located((By.ID, 'com.zhongsu.online:id/et_user_account')))
        self.driver.find_element_by_id('com.zhongsu.online:id/et_user_account').send_keys(1452535)
        self.driver.find_element_by_id('com.zhongsu.online:id/tbt_get_check_code').click()
        self.assertEqual('请输入正确的手机号', toast.get_toast_text(self, toast='请输入正确的手机号'))
        self.driver.find_element_by_id('com.zhongsu.online:id/et_user_account').clear()
        # 未注册的手机号
        self.driver.find_element_by_id('com.zhongsu.online:id/et_user_account').send_keys(13777622263)
        self.driver.find_element_by_id('com.zhongsu.online:id/tbt_get_check_code').click()
        self.assertEqual('无相关数据', toast.get_toast_text(self, toast='无相关数据'))
        self.driver.find_element_by_id('com.zhongsu.online:id/et_user_account').clear()
        # 已注册的手机号
        self.driver.find_element_by_id('com.zhongsu.online:id/et_user_account').send_keys(19957856328)
        self.driver.find_element_by_id('com.zhongsu.online:id/tbt_get_check_code').click()
        result = self.driver.find_element_by_id('com.zhongsu.online:id/tbt_get_check_code').text
        self.assertIn('重新发送', result)
        self.driver.find_element_by_id('com.zhongsu.online:id/et_check_code').send_keys(666666)
        # 2次输入的密码不一致
        self.driver.find_element_by_id('com.zhongsu.online:id/et_user_password').send_keys('a000000')
        self.driver.find_element_by_id('com.zhongsu.online:id/et_user_submit_password').send_keys('a0000001')
        time.sleep(1)
        self.driver.find_element_by_id('com.zhongsu.online:id/btn_submit').click()
        self.assertEqual('请确认密码是否保持一致', toast.get_toast_text(self, toast='请确认密码是否保持一致'))
        # 密码格式不正确
        self.driver.find_element_by_id('com.zhongsu.online:id/et_user_password').clear()
        self.driver.find_element_by_id('com.zhongsu.online:id/et_user_password').send_keys('a0000')
        self.driver.find_element_by_id('com.zhongsu.online:id/et_user_submit_password').clear()
        self.driver.find_element_by_id('com.zhongsu.online:id/et_user_submit_password').send_keys('a0000')
        self.driver.find_element_by_id('com.zhongsu.online:id/btn_submit').click()
        self.assertEqual('密码要求数字、字母以及标点符号(除空格)至少包含2种且长度为6-32之间',
                         toast.get_toast_text(self, toast='密码要求数字、字母以及标点符号(除空格)至少包含2种且长度为6-32之间'))
        # 密码修改成功
        pas = RndPassword.password(self)
        self.driver.find_element_by_id('com.zhongsu.online:id/et_user_password').clear()
        self.driver.find_element_by_id('com.zhongsu.online:id/et_user_password').send_keys('a' + pas)
        self.driver.find_element_by_id('com.zhongsu.online:id/et_user_submit_password').clear()
        self.driver.find_element_by_id('com.zhongsu.online:id/et_user_submit_password').send_keys('a' + pas)
        self.driver.find_element_by_id('com.zhongsu.online:id/btn_submit').click()
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_id('com.zhongsu.online:id/now_approve_tv').click()
        WebDriverWait(self.driver, 20, 0.5).until(
            EC.presence_of_element_located((By.ID, 'com.zhongsu.online:id/et_user_account')))
        self.driver.find_element_by_id('com.zhongsu.online:id/et_user_account').clear()
        self.driver.find_element_by_id('com.zhongsu.online:id/et_user_account').send_keys(19957856328)
        self.driver.find_element_by_id('com.zhongsu.online:id/et_user_password').send_keys('a' + pas)
        self.driver.find_element_by_id('com.zhongsu.online:id/btn_submit_login').click()
        # self.driver.implicitly_wait(20)
        # self.driver.find_element_by_id('com.zhongsu.online:id/tv_skip').click()
        WebDriverWait(self.driver, 20, 0.5).until(
            EC.presence_of_element_located((By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout'
                                                      '/android.widget.FrameLayout/android.widget.LinearLayout'
                                                      '/android.widget.FrameLayout/android.widget.RelativeLayout'
                                                      '/android.widget.HorizontalScrollView/android.widget.LinearLayout'
                                                      '/android.widget.LinearLayout[5]/android.widget.LinearLayout'
                                                      '/android.widget.ImageView')))
        self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout'
                                          '/android.widget.FrameLayout/android.widget.LinearLayout'
                                          '/android.widget.FrameLayout/android.widget.RelativeLayout'
                                          '/android.widget.HorizontalScrollView/android.widget.LinearLayout'
                                          '/android.widget.LinearLayout[5]/android.widget.LinearLayout'
                                          '/android.widget.ImageView').click()
        self.driver.implicitly_wait(20)
        result = self.driver.find_element_by_id('com.zhongsu.online:id/tv_account_name').text
        self.assertEqual("TEMPUSER_33xaki", result)



















    # def test02(self):
    #     # 未勾选保密协议提示确认后才登录
    #     self.d.implicitly_wait(20)
    #     self.d(resourceId="com.zhongsu.online:id/btn_login").click()
    #     self.d.implicitly_wait(20)
    #     self.d(resourceId="com.zhongsu.online:id/btn_submit_login").click()
    #     self.d.implicitly_wait(20)
    #     self.d(resourceId="com.zhongsu.online:id/now_approve_tv").click()
    #     self.d.implicitly_wait(20)
    #     # 输入错误验证码
    #     self.d.send_keys("123456", clear=True)
    #
    #     self.d(resourceId="com.zhongsu.online:id/img_finish").click()





if __name__ == '__main__':
    APP_pre.main()