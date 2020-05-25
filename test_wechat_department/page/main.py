"""
如果公司有web页面，直接使用这节课所学知识，试着为公司的页面做自动化测试。
如果没有则使用po思想，编写通讯录页面的测试用例，不可以有强制等待,driver需要封装到basepage中
有能力多写的人就多写，至少写一条，比如进入通讯录->设置所在部门
提醒：
企业微信页面定位有很多坑。碰到这些坑使用xpath可能是更好的选择。
"""

from selenium.webdriver.common.by import By
from test_selenium.test_wechat_department.page.basepage import BasePage
from test_selenium.test_wechat_department.page.select_department import SelectDepartment


class Main(BasePage):  # 继承BasePage类

    # 给“设置所在部门”按钮建模
    def goto_selectdepartment(self):
        # 勾选需要设置的人
        ele = self.find(By.XPATH, '//*[@id="member_list"]/tr[1]//input')  # 这里找到第一个人前面的勾选框元素
        ele.click()  # 点击该元素
        self.wait_selected(ele)  # 调用隐式等待方法，直到该元素被选择————这里显等成功
        # 点击设置所在部门
        self.find(By.CSS_SELECTOR, '.js_move').click()

        # 进入选择范围弹框
        return SelectDepartment(self.driver)  # 这里相当于实例化SelectDepartment类，并传入self.driver

