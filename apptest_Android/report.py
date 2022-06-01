from HTMLTestRunner_cn import HTMLTestRunner  # github中有收藏
import unittest
import time
import os
from apptest_Android.Mine import APP_my_provision
from apptest_Android.Mine import APP_SalesManagement
import sys

suit = unittest.TestSuite()
testcase = unittest.TestLoader().loadTestsFromModule(APP_my_provision)  # 存在多个类时要运行整个文件用这个方法
suit.addTest(testcase)
path = os.path.join(os.getcwd())
print(path)
# 自动搜索项目根目录下的所有case，构造测试集；返回TestSuit对象
discover = unittest.defaultTestLoader.discover(path, pattern="IM*.py")
# 然后HTMLTestRunner执行容器中的用例，然后生成测试报告
time = time.strftime("%Y-%m-%d %H_%M_%S")
file = time+'测试.html'
f = open('C:/Users/msi/Documents/测试报告/%s_report.html' % time, 'wb')
runner = HTMLTestRunner(
    stream=f,
    verbosity=2,
    title='unittest报告',
    description='练习HTMLTestRunner的使用',
    retry=0,  # 失败以后重试次数
    # save_last_try=True,
    # save_last_try 为True ，一个用例仅显示最后一次测试的结果；为false，则显示所有重试的结果。


)

runner.run(suit)
# runner.run(discover)