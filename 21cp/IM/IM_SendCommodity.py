import paramunittest
import time
import ready_login
from selenium.common.exceptions import NoSuchElementException


class SendCommodityTest(ready_login.TestClass):

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
        # 发送原料
        nu = 1
        while nu <= 60:
            try:
                self.driver.implicitly_wait(20)
                self.driver.find_element_by_xpath('//*[@id="chat-edit"]/div/div/div[1]/div[4]/div[1]').click()
                self.driver.implicitly_wait(20)
                expect = self.driver.find_element_by_xpath(
                    '//*[@id="chat-edit"]/div/div/div[1]/div[4]/div[2]/div/div[2]/div/div/div[1]/div[3]/div[1]/div[1]/div[2]').text
                self.driver.find_element_by_xpath(
                    '//*[@id="chat-edit"]/div/div/div[1]/div[4]/div[2]/div/div[2]/div/div/div[1]/div[3]/div[1]/div[1]/div[1]').click()
                self.driver.find_element_by_xpath(
                    '//*[@id="chat-edit"]/div/div/div[1]/div[4]/div[2]/div/div[2]/div/div/div[2]/button[1]').click()
                time.sleep(2)
                line = len(self.driver.find_elements_by_xpath('//*[@id="chat-list"]/div[1]/div/div'))

                result = self.driver.find_element_by_xpath(
                    '//*[@id="chat-list"]/div[1]/div/div[%s]/div/div[2]/div/a/div[1]/h3' % str(line-1)).text
                self.assertIn(expect, result)
                break
            except Exception as error:
                print(error)
                nu += 1

    def test_02(self):
        # 发送废塑料
        nu = 1
        while nu <= 60:
            try:
                self.driver.implicitly_wait(20)
                self.driver.find_element_by_xpath('//*[@id="chat-edit"]/div/div/div[1]/div[4]/div[1]').click()
                self.driver.implicitly_wait(20)
                self.driver.find_element_by_xpath(
                    '//*[@id="chat-edit"]/div/div/div[1]/div[4]/div[2]/div/div[2]/div/div/div[1]/div[2]/div[4]').click()
                time.sleep(3)
                expect = self.driver.find_element_by_xpath(
                    '//*[@id="chat-edit"]/div/div/div[1]/div[4]/div[2]/div/div[2]/div/div/div[1]/div[3]/div/div[1]/div[2]').text
                print(expect)
                time.sleep(2)
                self.driver.find_element_by_xpath(
                    '//*[@id="chat-edit"]/div/div/div[1]/div[4]/div[2]/div/div[2]/div/div/div[1]/div[3]/div/div[1]/div[1]').click()
                self.driver.find_element_by_xpath(
                    '//*[@id="chat-edit"]/div/div/div[1]/div[4]/div[2]/div/div[2]/div/div/div[2]/button[1]').click()
                time.sleep(2)
                line = len(self.driver.find_elements_by_xpath('//*[@id="chat-list"]/div[1]/div/div'))

                result = self.driver.find_element_by_xpath(
                    '//*[@id="chat-list"]/div[1]/div/div[%s]/div/div[2]/div/a/div[1]/h3' % str(line - 1)).text
                self.assertEqual(expect, result)
                break
            except Exception as error:
                print(error)
                nu += 1

    # 点击进入商品详情
    def test_03(self):
        nu = 1
        while nu <= 60:
            try:
                line = len(self.driver.find_elements_by_xpath('//*[@id="chat-list"]/div[1]/div/div'))

                expect = self.driver.find_element_by_xpath(
                    '//*[@id="chat-list"]/div[1]/div/div[%s]/div/div[2]/div/a/div[1]/h3' % str(line - 1)).text
                self.driver.find_element_by_xpath(
                    '//*[@id="chat-list"]/div[1]/div/div[%s]/div/div[2]/div/a' % str(line - 1)).click()
                handles = self.driver.window_handles
                self.driver.switch_to_window(handles[-1])
                result = self.driver.title
                for window in handles:
                    self.driver.switch_to.window(window)
                    if self.driver.title == "说塑聊料":
                        break
                self.assertIn(expect, result)
                break
            except Exception as error:
                print(error)
                nu += 1

    # 发送可供
    def test_04(self):
        nu = 1
        while nu <= 60:
            try:
                self.driver.implicitly_wait(20)
                self.driver.find_element_by_xpath('//*[@id="chat-edit"]/div/div/div[1]/div[5]/div[1]').click()
                self.driver.implicitly_wait(20)
                expect = self.driver.find_element_by_xpath(
                    '//*[@id="chat-edit"]/div/div/div[1]/div[5]/div[2]/div/div[2]/div/div/div[1]/div[3]/div/div[1]/div[2]').text
                self.driver.find_element_by_xpath(
                    '//*[@id="chat-edit"]/div/div/div[1]/div[5]/div[2]/div/div[2]/div/div/div[1]/div[3]/div/div[1]/div[1]').click()
                self.driver.find_element_by_xpath(
                    '//*[@id="chat-edit"]/div/div/div[1]/div[5]/div[2]/div/div[2]/div/div/div[2]/button[1]').click()
                line = len(self.driver.find_elements_by_xpath('//*[@id="chat-list"]/div[1]/div/div'))

                result = self.driver.find_element_by_xpath(
                    '//*[@id="chat-list"]/div[1]/div/div[%s]/div/div[2]/div/a/div[1]/h3' % str(line - 1)).text
                self.assertIn(expect, result)
                break
            except Exception as error:
                print(error)
                nu += 1

    # 点击可供进入企业产品
    def test_05(self):
        nu = 1
        while nu <= 60:
            try:
                line = len(self.driver.find_elements_by_xpath('//*[@id="chat-list"]/div[1]/div/div'))
                expect = self.driver.find_element_by_xpath(
                    '//*[@id="chat-list"]/div[1]/div/div[%s]/div/div[2]/div/a/div[1]/h3' % str(line - 1)).text
                self.driver.find_element_by_xpath(
                    '//*[@id="chat-list"]/div[1]/div/div[%s]/div/div[2]/div/a' % str(line - 1)).click
                handles = self.driver.window_handles
                self.driver.switch_to_window(handles[-1])
                result = self.driver.title
                self.assertIn(expect, result)
                break
            except Exception as error:
                print(error)
                nu += 1


if __name__ == '__main__':
    ready_login.main()
