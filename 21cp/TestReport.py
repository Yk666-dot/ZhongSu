from HTMLTestRunner import HTMLTestRunner
import unittest
import time
import os
import IM_SendMessage


suit = unittest.TestSuite()
testcase = unittest.TestLoader().loadTestsFromModule(IM_SendMessage)  # 存在多个类时要运行整个文件用这个方法
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
    tester='俞锴'
)

runner.run(suit)
# runner.run(discover)