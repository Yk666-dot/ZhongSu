from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def get_toast_text(self, toast):
    loc = '//*[contains(@text,"{}")]'.format(toast)

    # 等待的时候，要用元素存在的条件。不能用元素可见的条件。
    WebDriverWait(self.driver, 20, 0.01).until(EC.presence_of_element_located((By.XPATH, loc)))
    # 上限10秒就够了，确认toast在页面上存在的时候大概是多久，它都没有0.5秒，你去间隔0.5，可能消失了，你还只留在这。
    return self.driver.find_element_by_xpath(loc).text