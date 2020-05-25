from selenium.webdriver.common.by import By
from test_selenium.test_wechat_department.page.basepage import BasePage


class Contact(BasePage):  # 继承BasePage类

    # 给通讯录页面建模
    def get_department(self):  # 显示所有成员信息
        # sleep(5)  ########### 强等生效
        # ele = (By.XPATH, '//*[@id="member_list"]/tr[1]/td[4]/span')  # 获取所操作人物对应的部门元素
        # self.wait_click(ele)  # 直到该元素可被点击——————显等失败
        self.refresh()  # 调用刷新方法
        text1 = self.find(By.XPATH, '//*[@id="member_list"]/tr[1]/td[4]/span').text
        print(text1)  # 获取该元素的文本信息
        print(type(text1))  # 打印文件信息的类型
        return text1  # 返回文本信息