"""
登录方式二：使用cookie登录（适合全自动化测试）
step1:获取cookie——driver.get_cookies()
step2：使用cookie
"""
import json
from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestLoginCookie:
    def setup(self):
        self.driver = webdriver.Chrome()  # 实例化Chrome类
        self.driver.implicitly_wait(3)  # 隐式等待
        self.driver.get("https://work.weixin.qq.com/")  # 打开网页

    def teardown(self):
        # self.driver.quit()  # 关闭网页
        pass

    # 定义get_cookie方法用于获取cookie
    def get_cookie(self):
        self.driver.find_element(By.CSS_SELECTOR, '.index_top_operation a:nth-child(1)').click()  # 获取企业登录按钮元素，并点击
        sleep(5)  # 强制等待5秒，趁此时间，扫描登录；最后等程序自动执行完，这样就获取到了登录的cookie
        cookie = self.driver.get_cookies()  # 获取当前页面的cookies，并赋值给cookie
        # print(cookie)
        with open("data.json", "w") as f:  # 新建data.json文件，重命名为f；用于存储获取到的cookie——持久化的存储cookie就是用文件存储
            json.dump(obj=cookie, fp=f)  # 把获取到的cookie存入到data.json文件中

    # 定义test_cookie_login方法，用于测试是否能成功使用获取到的cookie
    def test_cookie_login(self):
        cookies = json.load(open("data.json"))  # 读取存储cookie的文件
        for cookie in cookies:  # 遍历cookies列表，把所有cookie添加到浏览器中
            if "expiry" in cookie:  # 如果expiry在cookie中，主要是解决invalid argument: invalid 'expiry'这个问题
                cookie.pop("expiry")  # 就把expiry删除
            self.driver.add_cookie(cookie)  # 每次只添加一个cookie
        sleep(2)  # 强制等待，用于等cookie全部加到浏览器中
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#contacts")  # 打开网页，检测是否成功使用cookie
        sleep(2)

if __name__ == '__main__':
    pytest.main()
