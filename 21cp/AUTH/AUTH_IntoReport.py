import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import ready_login
import PARM


class IntoReportTest(ready_login.TestClass):

    # 从平台企业库进入
    def test_01(self):
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_xpath('/html/body/div[3]/div[2]/ul[1]/li[4]/a').click()
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_id('searchText').send_keys('余姚')
        self.driver.find_element_by_id('searchSubmit').click()
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_class_name('sell-icon').click()
        self.driver.implicitly_wait(20)
        sid = self.driver.find_element_by_xpath(
            '/html/body/div[5]/div[4]/div[1]/div[2]/div[2]/div[1]/div[2]/a').get_attribute('data-accountsid')
        result = self.driver.find_element_by_xpath(
            '/html/body/div[5]/div[4]/div[1]/div[2]/div[2]/div[1]/div[3]/a[2]').get_attribute('href')
        self.assertEqual('https://shop.21cp.work/authentication/%s.html' % sid, result)

    # 再生料频道进入
    def test_02(self):
        # 再生料列表页进入
        self.driver.find_element_by_xpath('//*[@id="allTopBar"]/div[2]/a[1]').click()
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_xpath('/html/body/div[4]/ul/li[5]/a').click()
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_xpath('//*[@id="nav"]/div/div[2]/div[2]/a[3]/div[1]').click()
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div[1]/div[1]/div[1]/a[2]').click()
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div[1]/div[1]/div[2]/div[8]/a/div[1]').click()
        self.driver.implicitly_wait(20)
        href = self.driver.find_element_by_xpath(
            '//*[@id="app"]/div[2]/div[2]/div[1]/div[3]/div[1]/div[1]/div[1]/div[2]/div[2]/a').get_attribute('href')
        sid = href[28:-5]
        result = self.driver.find_element_by_xpath(
            '//*[@id="app"]/div[2]/div[2]/div[1]/div[3]/div[1]/div[1]/div[1]/div[2]/a').get_attribute('href')
        self.assertEqual('https://shop.21cp.work/authentication/%s.html' % sid, result)
        # 再生料详情页
        self.driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/a').click()
        self.driver.implicitly_wait(20)
        result = self.driver.find_element_by_xpath(
            '//*[@id="app"]/div[2]/div[2]/div[2]/div[1]/div[3]/a').get_attribute('href')
        self.assertEqual('https://shop.21cp.work/authentication/%s.html' % sid, result)

    # 从搜索列表进入
    def test_03(self):
        self.driver.find_element_by_xpath('//*[@id="allTopBar"]/div[2]/a[1]').click()
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_id('searchText').send_keys(PARM.search)
        self.driver.find_element_by_id('searchSubmit').click()
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_xpath('/html/body/div[7]/div[1]/div[1]/div[1]/div[2]/a[2]/i').click()
        self.driver.implicitly_wait(20)
        i = 1
        while i > 0:
            cla = self.driver.find_element_by_xpath(
                '/html/body/div[7]/div[1]/div[2]/div/div[%s]' % i).get_attribute('class')
            if 'recommended_item' not in cla:
                break
            i += 1
        sid = self.driver.find_element_by_xpath(
            '/html/body/div[7]/div[1]/div[2]/div/div[%s]/div[1]/div' % i).get_attribute('data-sid')
        result = self.driver.find_element_by_xpath(
            '/html/body/div[7]/div[1]/div[2]/div/div[%s]/div[5]/a' % i).get_attribute('href')
        self.assertEqual('https://shop.21cp.work/authentication/%s.html' % sid, result)

    # 供应列表进入
    def test_04(self):
        self.driver.find_element_by_xpath('//*[@id="allTopBar"]/div[2]/a[1]').click()
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_xpath('/html/body/div[4]/ul/li[2]/a').click()
        self.driver.implicitly_wait(20)
        i = 1
        while i > 0:
            text = self.driver.find_element_by_xpath('/html/body/div[5]/div[2]/div[1]/div[1]/div[2]/a[%s]' % i).text
            if text == "ABS":
                break
            i += 1
        self.driver.find_element_by_xpath('/html/body/div[5]/div[2]/div[1]/div[1]/div[2]/a[%s]' % i).click()
        handles = self.driver.window_handles
        self.driver.switch_to_window(handles[-1])
        self.driver.implicitly_wait(20)
        target = self.driver.find_element_by_xpath('/html/body/div[6]/div[1]/div[6]/div[2]')
        self.driver.execute_script("arguments[0].scrollIntoView();", target)
        i = 1
        while i >= 1:
            title = self.driver.find_element_by_xpath(
                '/html/body/div[6]/div[1]/div[6]/div[2]/div[2]/a[%s]' % i).get_attribute('title')
            if title == '0215A/吉林石化':
                break
            i += 1
        self.driver.find_element_by_xpath('/html/body/div[6]/div[1]/div[6]/div[2]/div[2]/a[%s]' % i).click()
        handles = self.driver.window_handles
        self.driver.switch_to_window(handles[-1])
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_xpath('//*[@id="guideModal"]/div[2]/a').click()
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_xpath('//*[@id="j-open1"]/div[4]/a[1]').click()
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_xpath('/html/body/div[5]/div[2]/div[3]/div/div[2]/a[2]/i').click()
        self.driver.implicitly_wait(20)
        sid = self.driver.find_element_by_xpath(
            '/html/body/div[5]/div[2]/div[4]/div/div/div[1]/div').get_attribute('data-sid')
        result = self.driver.find_element_by_xpath(
            '/html/body/div[5]/div[2]/div[4]/div/div/div[5]/a').get_attribute('href')
        self.assertEqual('https://shop.21cp.work/authentication/%s.html' % sid, result)
        # 从详情页进入
        self.driver.find_element_by_xpath('/html/body/div[5]/div[2]/div[4]/div/div/div[1]/h4/a').click()
        handles = self.driver.window_handles
        self.driver.switch_to_window(handles[-1])
        self.driver.implicitly_wait(20)
        result = self.driver.find_element_by_xpath(
            '/html/body/div[5]/div[2]/div[1]/div[1]/div[2]/ul/li[6]/a').get_attribute('href')
        self.assertEqual('https://shop.21cp.work/authentication/%s.html' % sid, result)





if __name__ == '__main__':
    ready_login.main()

