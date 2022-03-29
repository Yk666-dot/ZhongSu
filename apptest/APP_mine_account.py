import APP_pre
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import random
import toast
import time
import wait
import create_data


class RndPassword:
    def email(self):
        i = 1
        lis = []
        while i <= 6:
            lis.append(str(random.randint(0, 9)))
            i += 1
        return ''.join(lis)


class MineTest(APP_pre.LoginTest):
    # 前置登录
    def test_01(self):
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_xpath(
            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout'
            '/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout'
            '/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.widget.LinearLayout[5]'
            '/android.widget.LinearLayout/android.widget.ImageView').click()
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_id('com.zhongsu.online:id/tv_click_login').click()
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

        # 账号信息用户账户确认
        self.driver.implicitly_wait(20)
        account = self.driver.find_element_by_id('com.zhongsu.online:id/tv_account_name').text
        self.driver.find_element_by_id('com.zhongsu.online:id/btn_account').click()

    #     self.driver.implicitly_wait(20)
    #     self.assertEqual(account, self.driver.find_element_by_id('com.zhongsu.online:id/tv_co_account_name').text)
    #
    # # 更换头像
    # def test_02(self):
    #     self.driver.find_element_by_id('com.zhongsu.online:id/im_co_head_pic').click()
    #     self.driver.implicitly_wait(20)
    #     self.driver.find_elements_by_id('com.zhongsu.online:id/tvCheck')[random.randint(1, 8)].click()
    #     self.driver.implicitly_wait(20)
    #     self.driver.find_element_by_id('com.zhongsu.online:id/picture_right').click()
    #     self.driver.implicitly_wait(20)
    #     self.driver.find_element_by_id('com.zhongsu.online:id/menu_crop').click()
    #     # 现在暂时只能用更换头像后是否返回账号信息页面来判断成功，看后续能不能优化
    #     self.driver.implicitly_wait(20)
    #     self.assertEqual('上传头像成功', toast.get_toast_text(self, toast='上传头像成功'))
    #
    # # 跳转修改账号
    # def test_03(self):
    #     self.driver.find_element_by_id('com.zhongsu.online:id/tv_co_account_name').click()
    #     self.driver.implicitly_wait(20)
    #     tip = self.driver.find_element_by_id('com.zhongsu.online:id/tv_tip').text
    #     self.assertIn('您已修改过一次', tip)
    #     self.driver.find_element_by_id('com.zhongsu.online:id/btn_submit').click()
    #
    # # 修改手机号
    # def test_04(self):
    #     self.driver.implicitly_wait(20)
    #     self.driver.find_element_by_id('com.zhongsu.online:id/tv_co_phone').click()
    #     self.driver.implicitly_wait(20)
    #     self.driver.find_element_by_id('com.zhongsu.online:id/btn_get_check_code').click()
    #     # 错误的验证码
    #     self.driver.find_element_by_id('com.zhongsu.online:id/et_check_code').send_keys('123456')
    #     self.driver.find_element_by_id('com.zhongsu.online:id/btn_submit').click()
    #     self.assertEqual('手机验证码错误', toast.get_toast_text(self, toast='手机验证码错误'))
    #     # 使用过的验证码不可再使用
    #     self.driver.find_element_by_id('com.zhongsu.online:id/et_check_code').clear()
    #     self.driver.find_element_by_id('com.zhongsu.online:id/et_check_code').send_keys('666666')
    #     self.driver.find_element_by_id('com.zhongsu.online:id/btn_submit').click()
    #     wait.wait_click(self, element='com.zhongsu.online:id/ib_back_layout_toolbar_back_righttv')
    #     wait.wait_click(self, element='com.zhongsu.online:id/btn_submit')
    #     self.assertEqual('手机验证码错误', toast.get_toast_text(self, toast='手机验证码错误'))
    #     # 更换输入的手机号为当前绑定的手机号
    #     wait.countdown(self, element='com.zhongsu.online:id/btn_get_check_code', tip="获取验证码")
    #     self.driver.find_element_by_id('com.zhongsu.online:id/btn_get_check_code').click()
    #     self.driver.find_element_by_id('com.zhongsu.online:id/btn_submit').click()
    #     self.driver.implicitly_wait(20)
    #     self.driver.find_element_by_id('com.zhongsu.online:id/et_new_phone').send_keys('18888648053')
    #     self.driver.find_element_by_id('com.zhongsu.online:id/btn_get_check_code').click()
    #     self.assertEqual('该手机已被使用！', toast.get_toast_text(self, toast='该手机已被使用！'))
    #     # 发送验证码后更换手机
    #     self.driver.find_element_by_id('com.zhongsu.online:id/et_new_phone').clear()
    #     self.driver.find_element_by_id('com.zhongsu.online:id/et_new_phone').send_keys('18928832771')
    #     self.driver.find_element_by_id('com.zhongsu.online:id/btn_get_check_code').click()
    #     self.driver.find_element_by_id('com.zhongsu.online:id/et_check_code').send_keys('666666')
    #     self.driver.find_element_by_id('com.zhongsu.online:id/et_new_phone').clear()
    #     self.driver.find_element_by_id('com.zhongsu.online:id/et_new_phone').send_keys('13722983392')
    #     self.driver.find_element_by_id('com.zhongsu.online:id/btn_submit').click()
    #     self.assertEqual('手机验证码错误', toast.get_toast_text(self, toast='手机验证码错误'))
    #     # 新手机验证码错误
    #     self.driver.find_element_by_id('com.zhongsu.online:id/et_new_phone').clear()
    #     self.driver.find_element_by_id('com.zhongsu.online:id/et_new_phone').send_keys('19022837728')
    #     wait.countdown(self, element='com.zhongsu.online:id/btn_get_check_code')
    #     self.driver.find_element_by_id('com.zhongsu.online:id/btn_get_check_code').click()
    #     self.driver.find_element_by_id('com.zhongsu.online:id/et_check_code').clear()
    #     self.driver.find_element_by_id('com.zhongsu.online:id/et_check_code').send_keys('123456')
    #     self.driver.find_element_by_id('com.zhongsu.online:id/btn_submit').click()
    #     self.assertEqual('手机验证码错误', toast.get_toast_text(self, toast='手机验证码错误'))
    #     self.driver.find_element_by_id('com.zhongsu.online:id/ib_back_layout_toolbar_back_righttv').click()
    #     time.sleep(3)
    #     self.driver.find_element_by_id('com.zhongsu.online:id/ib_back_layout_toolbar_back_righttv').click()

    # # 更换用户邮箱
    # def test_05(self):
    #     self.driver.implicitly_wait(20)
    #     self.driver.find_element_by_id('com.zhongsu.online:id/btn_email').click()
    #     # 邮箱格式正确
    #     self.driver.find_element_by_id('com.zhongsu.online:id/et_email').send_keys('12345627736')
    #     self.driver.find_element_by_id('com.zhongsu.online:id/btn_get_check_code').click()
    #     self.assertEqual('请输入正确的邮箱', toast.get_toast_text(self, toast='请输入正确的邮箱'))
    #     # 更改为正在使用的邮箱
    #     self.driver.find_element_by_id('com.zhongsu.online:id/et_email').clear()
    #     email = self.driver.find_element_by_id('com.zhongsu.online:id/tv_old_email').text
    #     self.driver.find_element_by_id('com.zhongsu.online:id/et_email').send_keys(email)
    #     self.driver.find_element_by_id('com.zhongsu.online:id/btn_get_check_code').click()
    #     self.assertEqual('该邮箱已被使用！', toast.get_toast_text(self, toast='该邮箱已被使用！'))
    #     # 将正在使用的邮箱改成大写
    #     self.driver.find_element_by_id('com.zhongsu.online:id/et_email').clear()
    #     self.driver.find_element_by_id('com.zhongsu.online:id/et_email').send_keys(email.upper())
    #     self.driver.find_element_by_id('com.zhongsu.online:id/btn_get_check_code').click()
    #     self.assertEqual('该邮箱已被使用！', toast.get_toast_text(self, toast='该邮箱已被使用！'))
    #     # 使用错误的验证码
    #     self.driver.find_element_by_id('com.zhongsu.online:id/et_email').clear()
    #     self.driver.find_element_by_id('com.zhongsu.online:id/et_email').send_keys(
    #         '%s@email.com' % RndPassword.email(self))
    #     self.driver.find_element_by_id('com.zhongsu.online:id/btn_get_check_code').click()
    #     self.driver.find_element_by_id('com.zhongsu.online:id/et_check_code').send_keys(666666)
    #     self.driver.find_element_by_id('com.zhongsu.online:id/btn_submit').click()
    #     self.assertEqual('邮箱验证码错误', toast.get_toast_text(self, toast='邮箱验证码错误'))
    #     # 发送验证码后换成其他邮箱
    #     self.driver.find_element_by_id('com.zhongsu.online:id/et_email').clear()
    #     self.driver.find_element_by_id('com.zhongsu.online:id/et_email').send_keys(
    #         '%s@email.com' % RndPassword.email(self))
    #     self.driver.find_element_by_id('com.zhongsu.online:id/btn_submit').click()
    #     self.assertEqual('邮箱验证码错误', toast.get_toast_text(self, toast='邮箱验证码错误'))
    #     # # 输入合法数据更换成功
    #     # wait.countdown(self, element='com.zhongsu.online:id/btn_get_check_code', tip='获取验证码')
    #     # self.driver.find_element_by_id('com.zhongsu.online:id/btn_get_check_code').click()
    #     # self.driver.find_element_by_id('com.zhongsu.online:id/btn_submit').click()
    #     self.driver.find_element_by_id('com.zhongsu.online:id/ib_back_layout_toolbar_back_righttv').click()

    # 联系人信息更换
    def test_06(self):
        self.driver.implicitly_wait(20)
        contact = self.driver.find_element_by_id('com.zhongsu.online:id/tv_contact_name').text
        self.driver.find_element_by_id('com.zhongsu.online:id/corp_contact_info').click()
        self.driver.implicitly_wait(20)
        # 联系人更换
        lis = self.driver.find_elements_by_xpath(
            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android'
            '.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget'
            '.RecyclerView/android.widget.RelativeLayout')
        while True:
            num = random.randint(1, len(lis))
            contact1 = self.driver.find_element_by_xpath(
                '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android'
                '.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview'
                '.widget.RecyclerView/android.widget.RelativeLayout['
                '%s]/android.widget.TextView[1]' % num).text
            if contact != contact1:
                break
        i = 1  # 顺便测试联系人必须选一个
        while i <= 2:
            self.driver.find_element_by_xpath(
                '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android'
                '.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget'
                '.RecyclerView/android.widget.RelativeLayout[%s]/android.widget.LinearLayout/android.widget.CheckBox' % num).click()
            i += 1
            time.sleep(1)
        self.driver.find_element_by_id('com.zhongsu.online:id/ib_back_layout_toolbar_back_righttv').click()
        self.assertEqual(wait.wait_text(self, element='com.zhongsu.online:id/tv_contact_name'), contact1)
        # 测试选中的联系人不可删除
        try:
            self.driver.find_element_by_xpath(
                '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android'
                '.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget'
                '.RecyclerView/android.widget.RelativeLayout[%s]/android.widget.LinearLayout/android.widget.TextView[2]' % num)

        except Exception as e:
            print(e)
            self.assertIn(
                'Message: An element could not be located on the page using the given search parameters.', format(e))

    # 新增编辑联系人
    def test_07(self):
        self.driver.find_element_by_xpath(
            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android'
            '.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView'
            '/android.widget.LinearLayout/android.widget.LinearLayout[3]/android.widget.LinearLayout['
            '1]/android.widget.TextView').click()
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_id('com.zhongsu.online:id/btn_right_layout_toolbar_back_righttv').click()
        self.driver.implicitly_wait(20)
        # 联系人为空不能保存
        self.driver.find_element_by_id('com.zhongsu.online:id/et_contact_phone').send_keys('188'+create_data.random_num(8))
        button = self.driver.find_element_by_id('com.zhongsu.online:id/btn_confirm').get_attribute('enabled')
        self.assertEqual('false', button)  # 断言按钮置灰
        # 手机号为空不能保存
        self.driver.find_element_by_id('com.zhongsu.online:id/et_contact_phone').send_keys("测试" + create_data.random_num(1))
        self.driver.find_element_by_id('com.zhongsu.online:id/et_contact_phone').clear()
        button = self.driver.find_element_by_id('com.zhongsu.online:id/btn_confirm').get_attribute('enabled')
        self.assertEqual('false', button)  # 断言按钮置灰
        # 手机号格式不正确
        self.driver.find_element_by_id('com.zhongsu.online:id/et_contact_phone').send_keys(62233626613)
        self.driver.find_element_by_id('com.zhongsu.online:id/btn_confirm').click()
        self.assertEqual('请输入正确的手机号码', toast.get_toast_text(self, toast='请输入正确的手机号码'))
        self.driver.find_element_by_id('com.zhongsu.online:id/et_contact_phone').clear()
        self.driver.find_element_by_id('com.zhongsu.online:id/et_contact_phone').send_keys(62233)
        self.driver.find_element_by_id('com.zhongsu.online:id/btn_confirm').click()
        self.assertEqual('请输入正确的手机号码', toast.get_toast_text(self, toast='请输入正确的手机号码'))












