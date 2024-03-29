import unittest
import uiautomator2 as u2
from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
# For W3C actions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from appium.webdriver.common.touch_action import TouchAction
import time
from Script import ElementExsit


class LoginTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # cls.d = u2.connect('OFTGSOYP4LU4NV49')
        # cls.d.app_start('com.zhongsu.online')
        caps = {}
        caps["platformName"] = "Android"
        caps["platformVersion"] = "9"
        caps["deviceName"] = "OFTGSOYP4LU4NV49"
        caps["appPackage"] = "com.zhongsu.online"
        caps["appActivity"] = "com.zhongsu.online.ui.main.activity.MainActivity"
        caps["ensureWebviewsHavePages"] = True
        caps["newCommandTimeout"] = 1200000
        caps["automationName"] = "UiAutomator2"
        caps['recreateChromeDriverSessions'] = True
        caps['skipServerInstallation'] = True
        caps['skipDeviceInitialization'] = True
        cls.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        cls.driver.implicitly_wait(20)
        el1 = cls.driver.find_element_by_id("com.zhongsu.online:id/tv_approve")
        el1.click()
        time.sleep(3)
        actions = ActionChains(cls.driver)
        actions.w3c_actions = ActionBuilder(cls.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        actions.w3c_actions.pointer_action.move_to_location(953, 775)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.move_to_location(86, 771)
        actions.w3c_actions.pointer_action.release()
        actions.perform()
        time.sleep(3)
        actions = ActionChains(cls.driver)
        actions.w3c_actions = ActionBuilder(cls.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        actions.w3c_actions.pointer_action.move_to_location(1005, 778)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.move_to_location(72, 758)
        actions.w3c_actions.pointer_action.release()
        actions.perform()
        time.sleep(3)
        el2 = cls.driver.find_element_by_id("com.zhongsu.online:id/guide_image")
        el2.click()
        try:
            cls.driver.implicitly_wait(5)
            cls.driver.find_element_by_id('com.zhongsu.online:id/cancel_act')
            text = "True"
        except:
            text = "False"
        if text == "True":
            cls.driver.find_element_by_id('com.zhongsu.online:id/cancel_act').click()

        # WebDriverWait(cls.driver, 30, 0.5).until(
        #    EC.presence_of_element_located((By.ID, 'com.zhongsu.online:id/img_cancel')))
        # cls.driver.find_element_by_id('com.zhongsu.online:id/img_cancel').click()
        cls.driver.implicitly_wait(20)
        cls.driver.find_element_by_xpath('//*[@resource-id="com.zhongsu.online:id/tab_layout"]'
                                         '/android.widget.LinearLayout[1]/android.widget.LinearLayout[5]'
                                         '/android.widget.LinearLayout[1]/android.widget.ImageView[1]').click()
        # cls.driver.implicitly_wait(20)
        # cls.driver.find_element_by_id('com.zhongsu.online:id/img_btn').click()
        # cls.driver.implicitly_wait(20)
        # cls.driver.find_element_by_id('com.zhongsu.online:id/img_btn').click()
        # cls.driver.implicitly_wait(20)
        # cls.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout'
        #                                  '/android.widget.FrameLayout/android.widget.LinearLayout'
        #                                  '/android.widget.FrameLayout/android.widget.RelativeLayout'
        #                                  '/androidx.viewpager.widget.ViewPager/android.widget.LinearLayout'
        #                                  '/android.view.ViewGroup/android.widget.ScrollView'
        #                                  '/android.widget.LinearLayout').click()

    def add_img(self):
        self.imgs.append(self.driver.get_screenshot_as_base64())
        return True

    def setUp(self):
        # 在是python3.x 中，如果在这里初始化driver ，因为3.x版本 unittest 运行机制不同，会导致用力失败时截图失败
        self.imgs = []
        self.addCleanup(self.cleanup)

    def cleanup(self):
        pass

    @classmethod
    def tearDownClass(cls):
        # cls.d.app_stop("com.addcn.android.house591")
        cls.driver.quit()
