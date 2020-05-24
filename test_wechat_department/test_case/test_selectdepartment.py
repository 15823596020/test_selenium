from test_selenium.test_wechat_department.page.main import Main


class TestSelectDepartment:

    def setup(self):
        self.main = Main()

    def test_selectdepartment(self):
        # assert "" in self.main.goto_selectdepartment().select_department().get_member()
        # pass
        self.main.goto_selectdepartment().select_department()

    def teardown(self):
        pass