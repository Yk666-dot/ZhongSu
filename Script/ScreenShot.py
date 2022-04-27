import time
import traceback


def getScreenShot(self, file, case):
    t = time.strftime("%Y-%m-%d %H_%M")
    self.driver.get_screenshot_as_file(
        r'C:\Users\msi\Pictures\Saved Pictures\%s\%s_%s.png' % (file, case, t))
    # format_exc()返回字符串，print_exc()则直接给打印出来
    raise Exception(traceback.format_exc())  # 主动抛出异常
