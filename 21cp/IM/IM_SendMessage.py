import paramunittest
import time
import ready_login
from selenium.webdriver.common.keys import Keys

message = "字数"
while len(message) <= 202:
    message = message + "字数"


@paramunittest.parametrized(
    {"msg": "飒飒何时能刚！@sad111", "msg1": message, "tip": "上传文件不能超过5MB！",
     "route": "C:/Users/msi/Pictures/9.jpg", "route1": "C:/Users/msi/Pictures/14.jpg",
     "route2": "C:/Users/msi/Documents/中心主题1_20210414_133137.xls",
     "route3": "C:/Users/msi/Documents/WXWork/1688850884710679/Cache/Video/2021-08/video(9).MP4"},

)
class SendmessageTest(ready_login.TestClass):

    def setParameters(self, msg, msg1, tip, route, route1, route2, route3):
        self.msg = msg
        self.msg1 = msg1
        self.tip = tip
        self.route = route
        self.route1 = route1
        self.route2 = route2
        self.route3 = route3

    # 发送消息
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
        # 点击回车发送
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_xpath('//*[@id="chat-edit"]/textarea').send_keys(self.msg)
        self.driver.find_element_by_xpath('//*[@id="chat-edit"]/textarea').send_keys(Keys.ENTER)
        nu = 1
        while nu <= 60:
            try:
                line = len(self.driver.find_elements_by_xpath('//*[@id="chat-list"]/div[1]/div/div'))
                result = self.driver.find_element_by_xpath(
                    '//*[@id="chat-list"]/div[1]/div/div[%s]/div/div[2]/div' % str(line)).text
                self.assertEqual(self.msg, result)
                break
            except Exception as error:
                print(error)
                print(nu)
                nu += 1
        # 点击按钮发送
        self.driver.find_element_by_xpath('//*[@id="chat-edit"]/textarea').send_keys(self.msg1)
        self.driver.find_element_by_xpath('//*[@id="chat-edit"]/button').click()
        nu = 1
        while nu <= 60:
            try:
                line = len(self.driver.find_elements_by_xpath('//*[@id="chat-list"]/div[1]/div/div'))
                result = self.driver.find_element_by_xpath(
                    '//*[@id="chat-list"]/div[1]/div/div[%s]/div/div[2]/div' % str(line)).text
                self.assertEqual(self.msg1, result)
                break
            except Exception as error:
                print(error)
                print(nu)
                nu += 1
        # result = self.driver.find_element_by_class_name('chatContent').text
        # self.assertIn(self.msg, result)
        # self.assertIn(self.msg1, result)

    # 使用常用语句
    def test_02(self):
        self.driver.find_element_by_xpath('//*[@id="chat-edit"]/div/div/div[1]/div[1]/div[1]').click()
        self.driver.implicitly_wait(20)
        xpath = '//*[@id="chat-edit"]/div/div/div[1]/div[1]/div[2]/div[2]/div/div[1]'
        expect = self.driver.find_element_by_xpath(xpath).text
        self.driver.find_element_by_xpath(xpath).click()
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="chat-edit"]/button').click()
        nu = 1
        while nu <= 60:
            try:
                line = len(self.driver.find_elements_by_xpath('//*[@id="chat-list"]/div[1]/div/div'))
                result = self.driver.find_element_by_xpath(
                    '//*[@id="chat-list"]/div[1]/div/div[%s]/div/div[2]/div' % str(line)).text
                self.assertEqual(expect, result)
                break
            except Exception as error:
                print(error)
                print(nu)
                nu += 1

    # 发送文件
    def test_03(self):
        self.driver.find_element_by_xpath('//*[@id="chat-edit"]/div/div/div[1]/div[2]/div/input').send_keys(self.route)
        nu = 1
        while nu <= 60:
            try:
                time.sleep(3)
                line = len(self.driver.find_elements_by_xpath('//*[@id="chat-list"]/div[1]/div/div'))
                img = self.driver.find_element_by_xpath(
                        '//*[@id="chat-list"]/div[1]/div/div[%s]/div/div[2]/div/div/img' % str(line))
                self.assertIn('100z100', img.get_attribute('src'))
                break
            except Exception as error:
                print(error)
                print(nu)
                nu += 1
        # 上传xls
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="chat-edit"]/div/div/div[1]/div[2]/div/input').send_keys(self.route2)
        nu = 1
        while nu <= 60:
            try:
                time.sleep(3)
                line = len(self.driver.find_elements_by_xpath('//*[@id="chat-list"]/div[1]/div/div'))
                img = self.driver.find_element_by_xpath(
                    '//*[@id="chat-list"]/div[1]/div/div[%s]/div/div[2]/div/a' % str(line))
                self.assertIn('中心主题1_20210414_133137.xls', img.get_attribute('title'))
                break
            except Exception as error:
                print(error)
                print(nu)
                nu += 1
        # 上传视频文件
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="chat-edit"]/div/div/div[1]/div[2]/div/input').send_keys(self.route3)
        nu = 1
        while nu <= 60:
            try:
                time.sleep(3)
                line = len(self.driver.find_elements_by_xpath('//*[@id="chat-list"]/div[1]/div/div'))
                video = self.driver.find_element_by_xpath(
                    '//*[@id="chat-list"]/div[1]/div/div[%s]/div/div[2]/div/video' % str(line))
                self.assertIn("video(9).MP4.MP4", video.get_attribute('src'))
                break
            except Exception as error:
                print(error)
                print(nu)
                nu += 1

    # 发送发票信息
    def test_04(self):
        time.sleep(3)
        self.driver.find_element_by_xpath('//*[@id="chat-edit"]/div/div/div[1]/div[7]/div[1]').click()
        self.driver.implicitly_wait(20)
        expect = self.driver.find_element_by_xpath(
            '//*[@id="chat-edit"]/div/div/div[1]/div[7]/div[2]/div/div[2]/div/div/div[1]/div/div[2]/div[1]/div[2]').text
        self.driver.find_element_by_xpath(
            '//*[@id="chat-edit"]/div/div/div[1]/div[7]/div[2]/div/div[2]/div/div/div[2]/button[1]').click()
        nu = 1
        while nu <= 60:
            try:
                time.sleep(3)
                line = len(self.driver.find_elements_by_xpath('//*[@id="chat-list"]/div[1]/div/div'))
                result = self.driver.find_element_by_xpath(
                    '//*[@id="chat-list"]/div[1]/div/div[%s]/div/div[2]/div/div/ul/li[2]/span' % str(line)).text
                self.assertEqual(expect, result)
                break
            except Exception as error:
                print(error)
                print(nu)
                nu += 1


if __name__ == '__main__':
    ready_login.main()

