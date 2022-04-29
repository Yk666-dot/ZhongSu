# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
import time
from appium.webdriver.common.mobileby import MobileBy
from datetime import datetime, timedelta



caps = {}
caps["platformName"] = "Android"
caps["platformVersion"] = "9.0.1"
caps["deviceName"] = "OFTGSOYP4LU4NV49"
caps["appPackage"] = "com.jingdong.app.mall"
caps["appActivity"] = ".main.MainActivity"
caps["ensureWebviewsHavePages"] = True
caps["noReset"] = True
caps["newCommandTimeout"] = 1200000

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)

time.sleep(10)
TouchAction(driver).tap(x=323, y=248).perform()
driver.implicitly_wait(30)
driver.find_element_by_id('com.jd.lib.search.feature:id/ah0').click()
driver.implicitly_wait(30)
el3 = driver.find_element_by_xpath(
    '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget'
    '.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/androidx.recyclerview.widget'
    '.RecyclerView/android.widget.RelativeLayout['
    '3]/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.RelativeLayout['
    '1]/android.widget.RelativeLayout')
el3.click()
driver.implicitly_wait(30)


def run_your_script():
    print(123)
    actions = ActionChains(driver)
    actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
    actions.w3c_actions.pointer_action.move_to_location(874, 2249)
    actions.w3c_actions.pointer_action.pointer_down()
    actions.w3c_actions.pointer_action.pause(0.1)
    actions.w3c_actions.pointer_action.release()
    actions.perform()
    driver.implicitly_wait(30)
    driver.find_element_by_id('com.jd.lib.settlement.feature:id/a05').click()
    driver.find_element_by_id('com.jd.lib.settlement.feature:id/a4q').click()


def countdown(deltaT, time_set):
    # deltaT: float, 剩余的时间
    # time_set: datetime object, 设定的时间

    print("\n调用程序的固定时间为：", time_set)

    while deltaT:
        minutes, seconds = divmod(deltaT, 60)  # 分钟数为deltaT➗60的商部分，秒钟数为余数部分
        hours = minutes // 60  # 小时数: 分钟数除以60的商
        minutes -= hours * 60  # 分钟数：分钟数减去小时*60
        # 以上做法的目的：将时分秒都化为0-60内的数字，美观。

        timeformat = '{:02d}:{:02d}:{:02d}'.format(hours, minutes, seconds)

        print("距离下次调用的剩余时间为：", timeformat, end='\r')
        # '\r'确保光标在起始位置，使得剩余时间不会一行行输出，美观
        time.sleep(1)  # 停顿一秒
        deltaT -= 1  # 时间减少一秒

    run_your_script()


# 以下设定的时间可由用户输入或配置文件提供，注意字符串与整型的类型转换
HOUR = 16
MINUTE = 0
SECOND = 0

while True:
    now = datetime.now()  # 获取现在的时间
    time_set = now.replace(hour=HOUR, minute=MINUTE, second=SECOND)  # 设置的时间

    # 如果现在的钟面时间（不考虑日期）早于设定的时间，时间差为:较晚时间减去较早时间
    # 比如现在的时间是8am，而设定的时间是9am，那么时间差为1小时
    if now < time_set:
        deltaT = (time_set - now).total_seconds()  # 单位：秒

    # 如果现在的钟面时间（不考虑日期）不早于设定的时间，时间差为:24小时减去上述时间差
    # 比如现在的时间是9am，而设定的时间是8am，那么时间差为23小时(24-(9-8))

    else:
        time_set = now.replace(day=now.day + 1, hour=HOUR, minute=MINUTE, second=SECOND)
        # 既然已经过了设定时间，那么日期应为第二天

        deltaT = (timedelta(hours=24) - (now - now.replace(hour=HOUR, minute=MINUTE, second=SECOND))).total_seconds()

    time_set = time_set.strftime('%Y-%m-%d %H:%M:%S')  # 将时间规范化：年-月-日 时:分:秒
    countdown(int(deltaT), time_set)  # 必须将deltaT转化为整型，否则在timeformat处会报错







