# 验证元素是否存在
def is_element_exsit_xpath(self, xpath):
    try:
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_xpath(xpath)
        return True
    except:
        return False


def is_element_exsit_id(self, id):
    try:
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_id(id)
        return True
    except:
        return False