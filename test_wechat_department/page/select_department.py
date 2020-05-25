from time import sleep
from selenium.webdriver.common.by import By
from test_selenium.test_wechat_department.page.basepage import BasePage
from test_selenium.test_wechat_department.page.contact import Contact


class SelectDepartment(BasePage):  # 继承BasePage类

    # 给“选择范围”弹框建模——选择部门
    def select_department(self):
        # 选择部门
        sleep(10)  # 强等成功
        # 找__dialog__MNDialog的窗体，并且窗体的style不包含空的下级子元素id就是需要的
        ele = self.find(By.XPATH, '//*[contains(@id,"__dialog__MNDialog") and not(contains(@style,"none"))] //*[@id="1688852935766558"]')  # 这里定位需要移动到的部门元素

        # self.wait_click(ele)  # 调用隐式等待方法，直到该元素可被点击————————显等失败
        # sleep(10)  # 强等成功
        ele.click()  # 选择该元素
        # 点击确认按钮
        # self.wait_selected(ele)  # 调用隐式等待方法，直到该元素被选择————————显等失败
        sleep(10)  # 强等成功
        self.find(By.CSS_SELECTOR, '.js_submit').click()  # 定位“确认”按钮，并点击
        # 返回通讯录界面
        return Contact(self.driver)  # 这里相当于实例化Contact类，并传入self.driver

    # 给“选择范围”弹框建模——取消选择的部门
    def cancel_department(self):
        # 选择部门
        sleep(10)  # 强等成功
        # 找__dialog__MNDialog的窗体，并且窗体的style不包含空的下级子元素id就是需要的
        ele = self.find(By.XPATH, '//*[contains(@id,"__dialog__MNDialog") and not(contains(@style,"none"))] //*[@id="1688852935766558"]')  # 这里定位需要移动到的部门元素
        # self.wait_click(ele)  # 调用隐式等待方法，直到该元素可被点击————————显等失败
        # sleep(10)  # 强等成功
        ele.click()  # 选择该元素
        # 点击确认按钮
        # self.wait_selected(ele)  # 调用隐式等待方法，直到该元素被选择————————显等失败
        sleep(10)  # 强等成功
        self.find(By.CSS_SELECTOR, '.js_submit').click()  # 定位“确认”按钮，并点击
        # 返回通讯录界面
        return Contact(self.driver)  # 这里相当于实例化Contact类，并传入self.driver