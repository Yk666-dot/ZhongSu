import paramunittest
import time
import ready_login
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class ChatHistoryTest(ready_login.TestClass):

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
            if self.driver.title == "说塑聊料":
                break
        time.sleep(4)
        # 校验搜索为空
        # Action = ActionChains(self.driver)
        # Action.move_by_offset(0, 0).perform()
        # Action.move_by_offset(1460, 788).click().perform()
        self.driver.find_element_by_xpath('//*[@id="chat-edit"]/div/div/div[2]/div').click()
        time.sleep(3)
        s = '！@#￥%%%%'
        self.driver.find_element_by_xpath('//*[@id="historyMsg"]/div[1]/input').send_keys(s)
        self.driver.find_element_by_xpath('//*[@id="historyMsg"]/div[1]/button').click()
        time.sleep(3)
        result = self.driver.find_element_by_xpath('//*[@id="historyMsg"]/div[2]').text
        self.assertEqual('没有找到“%s”相关结果' % s, result)
        # 显示等待
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH,'//*[@id="historyMsg"]/div[1]/input')))
        finally:
            self.driver.find_element_by_xpath('//*[@id="historyMsg"]/div[1]/input').send_keys(Keys.CONTROL, 'a')

    def test_02(self):
        # 正常搜索
        self.driver.find_element_by_xpath('//*[@id="historyMsg"]/div[1]/input').send_keys("字数")
        self.driver.find_element_by_xpath('//*[@id="historyMsg"]/div[1]/button').click()
        self.driver.implicitly_wait(20)
        results = self.driver.find_elements_by_xpath('//*[@id="historyMsg"]/div[2]/div[1]/div')
        if len(results) == 0:
            print("无搜索结果")
        else:
            for i in range(1, len(results)+1):
                result = self.driver.find_element_by_xpath('//*[@id="historyMsg"]/div[2]/div[1]/div/div[%s]/div[2]/div[2]' % str(i+1))
                self.driver.execute_script("arguments[0].scrollIntoView();", result)
                self.assertIn("字数", result.text)



