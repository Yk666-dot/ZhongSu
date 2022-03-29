import time


def wait_click(self, element):
    i = 1
    while i <= 60:
        try:
            self.driver.find_element_by_id(element).click()
            break
        except Exception as error:
            print(error)
            time.sleep(1)
            i += 1


def wait_text(self, element):
    i = 1
    while i <= 60:
        try:
            text = self.driver.find_element_by_id(element).text
            return text
            break
        except Exception as error:
            print(error)
            time.sleep(1)
            i += 1


# 通过定位文本内容核实，如等待验证码按钮倒计时结束
def countdown(self, element, tip):
    while True:
        if self.driver.find_element_by_id(element).text == tip:
            break
        else:
            time.sleep(1)