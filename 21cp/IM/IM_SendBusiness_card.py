import paramunittest
import time
import ready_login


class SendBusinessTest(ready_login.TestClass):

    # 发送名片
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
        self.driver.find_element_by_xpath('//*[@id="chat-edit"]/div/div/div[1]/div[6]/div[1]').click()
        self.driver.implicitly_wait(20)
        expect = self.driver.find_element_by_xpath(
            '//*[@id="chat-edit"]/div/div/div[1]/div[6]'
            '/div[2]/div/div[2]/div/div/div[1]/div/div[2]/div[2]/div[2]/div[1]').text
        self.driver.find_element_by_xpath(
             '//*[@id="chat-edit"]/div/div/div[1]/div[6]/div[2]/div/div[2]/div/div/div[1]/div/div[2]/div[1]').click()
        self.driver.find_element_by_xpath('//*[@id="chat-edit"]/div/div/div[1]/div[6]/div[2]/div/div[2]/div'
                                          '/div/div[2]/button[1]').click()
        self.driver.implicitly_wait(20)
        line = len(self.driver.find_elements_by_xpath('//*[@id="chat-list"]/div[1]/div/div'))
        print(line)
        result1 = self.driver.find_element_by_xpath(
            '//*[@id="chat-list"]/div[1]/div/div[%i]/div/div[2]/div/div/div[1]/div[1]/h3' % int(line+1)).text
        self.assertEqual(expect, result1)
    # 点击名片进行洽谈
        self.driver.find_element_by_xpath('//*[@id="chat-list"]/div[1]/div/div[%i]/div/div[2]' % int(line+1)).click()
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/div[4]/div/div[2]/div/button').click()
        result = self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/div[1]/div[1]/strong').text
        print(result1)
        self.assertEqual(result1, result)

