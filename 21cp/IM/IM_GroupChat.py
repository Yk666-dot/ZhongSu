import paramunittest
import time
import ready_login
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

@paramunittest.parametrized(
    {"people_number": 4,
     "name": "！@123测试",
     "name01": "测试测试测试测试测试测试测试测试测试测试测试测试测试"},

)
class GroupChatTest(ready_login.TestClass):
    def setParameters(self, people_number, name, name01):
        self.people_number = people_number
        self.name = name
        self.name01 = name01

    def test_01(self):
        global member01, member02, member03
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
        time.sleep(2)
        member01 = self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/div[1]/div[1]/strong').text
        member02 = self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[1]/div[1]/div[2]/div[1]').text
        self.driver.find_element_by_xpath('//*[@id="chat-edit"]/div/div/div[1]/div[3]/div[1]').click()
        self.driver.implicitly_wait(20)
        num = self.driver.find_elements_by_xpath(
            '//*[@id="chat-edit"]/div/div/div[1]/div[3]/div[2]/div/div[2]/div/div/div[1]/div/div')
        # 子账号数量校验
        self.assertEqual(len(num), self.people_number)
        member03 = self.driver.find_element_by_xpath(
            '//*[@id="chat-edit"]/div/div/div[1]/div[3]/div[2]/div/div[2]/div/div/div[1]/div/div[3]/div[2]/div[2]/div[1]').text

    def test_02(self):
        # 创建群聊
        self.driver.find_element_by_xpath(
            '//*[@id="chat-edit"]/div/div/div[1]/div[3]/div[2]/div/div[2]/div/div/div[1]/div/div[3]/div[1]').click()
        self.driver.find_element_by_xpath(
            '//*[@id="chat-edit"]/div/div/div[1]/div[3]/div[2]/div/div[2]/div/div/div[2]/button[1]').click()
        members = member02 + ',' + member01 + ',' + member03
        time.sleep(3)
        result = self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/div[1]/div[1]/strong').text
        self.assertEqual(members, result)

    def test_03(self):
        # 重复邀请
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/div[1]/div[2]/button').click()
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_xpath('//*[@id="team_option"]/div[1]/div[1]/div/div/ul/li[1]/i').click()
        self.driver.implicitly_wait(20)
        i = 1
        while i > 0:
            try:
                result = self.driver.find_element_by_xpath(
                    '//*[@id="team_option"]/div[1]/div[1]/div/div/div/div/div[2]/div/div[1]/div/ul/li[%s]'% str(i))
                if member03 in result.text:
                    break
                i += 1
            except:
                print("无法邀请同事")
        self.assertEqual("disabled", result.get_attribute("class"))
        self.driver.find_element_by_xpath('//*[@id="team_option"]/div[1]/div[1]/div/div/div/div/div[1]/button').click()

    def test_04(self):
        # 修改群聊名称超过12字
        self.driver.find_element_by_xpath('//*[@id="team_option"]/div[2]/ul/li[1]/a/span').click()
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_xpath(
            '//*[@id="team_option"]/div[2]/div/div/div[2]/div/input').send_keys(Keys.CONTROL, "a")
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_xpath('//*[@id="team_option"]/div[2]/div/div/div[2]/div/input').send_keys(self.name01)
        self.driver.find_element_by_xpath('//*[@id="team_option"]/div[2]/div/div/div[3]/div/button[2]').click()
        time.sleep(3)
        result = self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/div[1]/div[1]/strong').text
        self.assertEqual(self.name01[0:16], result)

    def test_05(self):
        # 设置置顶
        self.driver.find_element_by_xpath('//*[@id="team_option"]/div[2]/ul/li[3]/a/div/span').click()
        time.sleep(3)
        result = self.driver.find_element_by_xpath(
            '//*[@id="app"]/div/div/div[2]/div[1]/div[2]/div[2]/div[1]/div/div[1]/div[1]/div[1]').text
        self.assertEqual(self.name01[0:16], result)

    def test_06(self):
        # 取消置顶
        self.driver.find_element_by_xpath('//*[@id="team_option"]/div[2]/ul/li[3]/a/div/span').click()
        time.sleep(3)
        result = self.driver.find_element_by_xpath(
            '//*[@id="app"]/div/div/div[2]/div[1]/div[2]/div[2]/div[1]/div/div[1]/div[1]/div[1]').text
        self.assertNotEqual(self.name01[0:16], result)

    def test_07(self):
        # 解散本群
        self.driver.find_element_by_xpath('//*[@id="team_option"]/div[2]/ul/li[4]/button').click()
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_xpath('/html/body/div[2]/div/div[3]/button[2]').click()
        time.sleep(2)
        result = self.driver.find_element_by_xpath('/html/body/div[3]/p').text
        self.assertNotIn("您已经解散本群", result)




