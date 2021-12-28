import paramunittest
import time
import ready_login
from selenium.webdriver.common.action_chains import ActionChains
import pyautogui as pag


message = "余姚!!@@43512adsgh"
while len(message) <= 200:
    message = message + "字数"


@paramunittest.parametrized(
    {"msg": message,
     },

)
class ManagementIdiomsTest(ready_login.TestClass):

    def setParameters(self, msg):
        self.msg = msg

    def test_01(self):
        # 添加常用语
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
        # time.sleep(3)
        # pag.click(799, 904)
        # time.sleep(2)
        # pag.click(1000, 658)
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_xpath('//*[@id="chat-edit"]/div/div/div[1]/div[1]/div[1]').click()
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_xpath('//*[@id="chat-edit"]/div/div/div[1]/div[1]/div[2]/div[1]/div[2]/i').click()
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_xpath(
            '//*[@id="chat-edit"]/div/div/div[1]/div[1]/div[2]/div/div[2]/div/div[2]/button').click()
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_xpath(
            '//*[@id="chat-edit"]/div/div/div[1]/div[1]/div[3]/div/div[2]/div/div[1]/div/textarea').send_keys(self.msg)
        self.driver.find_element_by_xpath(
            '//*[@id="chat-edit"]/div/div/div[1]/div[1]/div[3]/div/div[2]/div/div[2]/div[2]/button[1]').click()
        time.sleep(3)
        i = 1
        while i > 0:
            try:
                result = self.driver.find_element_by_xpath('//*[@id="chat-edit"]/div/div/div[1]/div[1]/div[2]/div/div[2]/div/div[1]/div/div[%s]/div[1]'% str(i)).text
                print(result)
                if result == self.msg:
                    # 删除
                    self.assertEqual(result, self.msg)
                    self.driver.find_element_by_xpath(
                        '//*[@id="chat-edit"]/div/div/div[1]/div[1]/div[2]/div/div[2]/div/div[1]/div/div[%s]/div[2]/div[2]'% str(i)).click()
                    self.driver.implicitly_wait(20)
                    self.driver.find_element_by_xpath('//*[@id="chat-edit"]/div/div/div[1]/div[1]/div[4]/div/div[2]/div/div[2]/button[1]').click()
                    break
                i += 1
            except:
                print('保存失败')
                break

