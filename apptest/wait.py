import time
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def wait_click(self, element, location):
    i = 1
    while i <= 60:
        try:
            if location == 'id':
                self.driver.find_element_by_id(element).click()
            elif location == 'xpath':
                self.driver.find_element_by_xpath(element).click()
            break
        except Exception as error:
            print(error)
            time.sleep(1)
            i += 1


def wait_text(self, element):
    i = 1
    while i <= 60:
        try:
            text = self.driver.find_element_by_id(element).text
            return text
            break
        except Exception as error:
            print(error)
            time.sleep(1)
            i += 1


# 通过定位文本内容核实，如等待验证码按钮倒计时结束
def countdown(self, element, tip):
    while True:
        if self.driver.find_element_by_id(element).text == tip:
            break
        else:
            time.sleep(1)


# 滑动至指定元素
def slide(self, text):
    return self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                    'new UiScrollable(new UiSelector().'
                                    'scrollable(true).instance(0)).'
                                    'scrollIntoView(new UiSelector().'
                                    'text("%s").instance(0));' % text)


# 显示等待  5秒内每隔0.5秒扫描一次页面，若不存在元素，则抛异常
def ExplicitWait(self, element):
    el = WebDriverWait(self.driver, 5, 0.5).until(lambda driver: driver.find_element_by_xpath(element))
    return el