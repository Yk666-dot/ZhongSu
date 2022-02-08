import paramunittest
import time
import ready_login
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


@paramunittest.parametrized(
    {"group": "余姚"},

)
class SearchTest(ready_login.TestClass):
    def setParameters(self, group):
        self.group = group

    # 搜索群名
    def test_01(self):
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_xpath('/html/body/div[3]/div[2]/ul[1]/li[4]/a').click()
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_class_name('placeholder').click()
        self.driver.implicitly_wait(20)
        self.driver.switch_to.active_element.send_keys('余姚')
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_id('searchSubmit').click()
        self.driver.implicitly_wait(20)
        target = self.driver.find_element_by_xpath('/html/body/div[5]/div[4]/div[1]/div[2]/div[2]/div[1]/div[5]/a')
        self.driver.execute_script("arguments[0].scrollIntoView();", target)  # 滚动条拖动到可见的元素去
        target.click()
        handles = self.driver.window_handles
        for window in handles:
            self.driver.switch_to.window(window)
            if self.driver.title == "中塑联机洽谈":
                break
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/div[2]/div[1]/input').send_keys("测试")
        time.sleep(3)
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/div[2]/div[1]/input').send_keys(Keys.ENTER)
        self.driver.implicitly_wait(20)
        i = len(self.driver.find_elements_by_xpath('//*[@id="app"]/div/div/div[2]/div[1]/div[2]/div[2]/div[1]/div/div'))
        # # chat_lis = []
        a = 1
        while a >= 1:
            try:
                title = self.driver.find_element_by_xpath(
                    '//*[@id="app"]/div/div/div[2]/div[1]/div[2]/div[2]/div[1]/div/div[%i]' % a).get_attribute('title')
                self.assertIn("测试", title)
            except:
                break
            a += 1

        self.assertEqual(a-1, i)


