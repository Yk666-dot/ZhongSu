import crm_login
import time
import phoneName


def test_01(self):
    # 创建客户
    self.driver.implicitly_wait(30)
    self.driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div[1]/div/ul/div[2]/li').click()
    self.driver.implicitly_wait(30)
    self.driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div[1]/div/ul/div[2]/li/ul/div[2]/a').click()
    self.driver.implicitly_wait(30)
    # 联系人
    self.driver.find_element_by_xpath(
        '//*[@id="app"]/div/div[2]/section/div/div/form/div[1]/div[2]/div/div/div/input').send_keys(phoneName.name())
    # 客户名称
    self.driver.find_element_by_xpath(
        '//*[@id="app"]/div/div[2]/section/div/div/form/div[2]/div/div/div/div[1]/input').send_keys(phoneName.company())
    # 移动电话
    self.driver.find_element_by_xpath(
        '//*[@id="app"]/div/div[2]/section/div/div/form/div[3]/div[1]/div/div/div/input').send_keys(phoneName.phone())
    # 所在地区一级
    self.driver.find_element_by_xpath(
        '//*[@id="app"]/div/div[2]/section/div/div/form/div[4]/div[1]/div/div/div/div[1]/div/div/input').click()
    self.driver.implicitly_wait(30)
    self.driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/ul/li[1]').click()
    # 所在地区二级
    self.driver.implicitly_wait(30)
    self.driver.find_element_by_xpath(
        '//*[@id="app"]/div/div[2]/section/div/div/form/div[4]/div[1]/div/div/div/div[2]/div/div/div/div/input').click()
    self.driver.implicitly_wait(30)
    self.driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[1]/ul/li').click()
    # 所在地区三级
    self.driver.implicitly_wait(30)
    self.driver.find_element_by_xpath(
        '//*[@id="app"]/div/div[2]/section/div/div/form/div[4]/div[1]/div/div/div/div[3]/div/div/div/div/input').click()
    self.driver.implicitly_wait(30)
    self.driver.find_element_by_xpath('/html/body/div[4]/div[1]/div[1]/ul/li[1]').click()
    # 详细地址
    self.driver.find_element_by_xpath(
        '//*[@id="app"]/div/div[2]/section/div/div/form/div[4]/div[2]/div/div/div/input').send_keys('马渚')
    # 选客户来源
    self.driver.find_element_by_xpath(
        '//*[@id="app"]/div/div[2]/section/div/div/form/div[5]/div[2]/div/div/div/div/input').click()
    self.driver.implicitly_wait(30)
    self.driver.find_element_by_xpath('/html/body/div[5]/div[1]/div[1]/ul/li[1]').click()
    # 选客户级别
    self.driver.find_element_by_xpath(
        '//*[@id="app"]/div/div[2]/section/div/div/form/div[5]/div[3]/div/div/div/div[1]/input').click()
    self.driver.implicitly_wait(30)
    self.driver.find_element_by_xpath('/html/body/div[6]/div[1]/div[1]/ul/li[1]').click()
    # 选主营产品
    self.driver.find_element_by_xpath(
        '//*[@id="app"]/div/div[2]/section/div/div/form/div[6]/div[1]/div/div[1]/div/div/div').click()
    self.driver.implicitly_wait(30)
    self.driver.find_element_by_xpath('//*[@id="pane-0"]/div/span[1]').click()
    self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div/div/div/div[1]/button').click()
    self.driver.implicitly_wait(30)
    # 选专业市场
    self.driver.find_element_by_xpath(
        '//*[@id="app"]/div/div[2]/section/div/div/form/div[7]/div[1]/div/div/div/div[1]/div/div[1]/input').click()
    self.driver.implicitly_wait(30)
    self.driver.find_element_by_xpath('/html/body/div[7]/div[1]/div[1]/ul/li[1]').click()
    self.driver.find_element_by_xpath(
        '//*[@id="app"]/div/div[2]/section/div/div/form/div[7]/div[1]/div/div/div/div[2]/div/div/div/div[1]/input').click()
    self.driver.implicitly_wait(30)
    self.driver.find_element_by_xpath('/html/body/div[8]/div[1]/div[1]/ul/li[1]').click()
    self.driver.find_element_by_xpath(
        '//*[@id="app"]/div/div[2]/section/div/div/form/div[7]/div[1]/div/div/div/div[3]/div/div/div/div[1]/input').click()
    self.driver.implicitly_wait(30)
    self.driver.find_element_by_xpath('/html/body/div[9]/div[1]/div[1]/ul/li[1]').click()
    # 选客户类型
    self.driver.find_element_by_xpath(
        '//*[@id="app"]/div/div[2]/section/div/div/form/div[8]/div[1]/div/div[1]/div/div/div/div[2]/input').click()
    self.driver.implicitly_wait(30)
    self.driver.find_element_by_xpath('/html/body/div[10]/div[1]/div[1]/ul/li[1]').click()
    self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div/form/div[9]/div[2]/button[1]').click()


if __name__ == '__main__':
   crm_login.main()



