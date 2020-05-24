from time import sleep

from selenium.webdriver import TouchActions
from selenium.webdriver.common.by import By

from test_selenium.test_wechat_department.page.basepage import BasePage
from test_selenium.test_wechat_department.page.contact import Contact


class SelectDepartment(BasePage):  # 继承BasePage类

    # 给“选择范围”弹框建模
    def select_department(self):
        # 选择部门//*[@id="1688852897171109_anchor"]  //*[@id="1688852927908152_anchor"]
        ele = self.find(By.XPATH, '//*[contains(@class,"ww_dialog_body")]//*[@id=1688852935766558]')  # 这里定位需要移动到的部门元素
        # self.wait_click(ele)  # 调用隐式等待方法，直到该元素可被点击
        sleep(10)
        ele.click()  # 选择该元素

        # 点击确认按钮
        # self.wait_selected(ele)  # 调用隐式等待方法，直到该元素被选择
        # self.find(By.XPATH, '//*[@id="__dialog__MNDialog_1590311162770__"]/div/div[3]/a[1]').click()
        #
        # 返回通讯录界面
        return Contact(self.driver)  # 这里相当于实例化Contact类，并传入self.driver