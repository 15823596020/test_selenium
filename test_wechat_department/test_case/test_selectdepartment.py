from test_selenium.test_wechat_department.page.basepage import BasePage
from test_selenium.test_wechat_department.page.main import Main


class TestSelectDepartment:  # 继承BasePage类
    def setup(self):
        self.main = Main()  # 实例化Main类

    def teardown(self):
        # self.main.quit()  # 调用BasePage类的quit方法，回收资源,case不要继承page，用实例化
        pass

    def test_selectdepartment(self):
        assert "test" in self.main.goto_selectdepartment().select_department().get_department()  # 断言被选择的部门在部门里面

    def test_canceldepartment(self):
        assert "test" not in self.main.goto_selectdepartment().cancel_department().get_department()  # 断言被取消的部门不在部门里面