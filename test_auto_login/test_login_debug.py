"""
登录方式一：复用已有浏览器（不适合全自动化，需要提前配置，只适合调式）
step1：关闭所有google浏览器
step2：找到Chrome的启动路径，右击google浏览器——属性——快捷方式——目标，chrome.exe之前的所有内容，即为启动路径
step3：把step2中找到的启动路径配置到环境变量中，重启命令行，输入chrome可验证环境变量是否配置成功
step4：在命令行中输入启动命令：chrome --remote_debugging-port=9222（该端口可以随便输入，只要不占用其他进程即可）
step5：在浏览器中输入localhost:9222可验证是否启动成功
"""
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class TestLoginDebug:
    def setup(self):
        option = Options()  # 实例化Options类
        option.debugger_address = "localhost:9222"  # 调用debugger_address方法，并传入调式地址为本地启动的一个服务，服务地址为localhost:9222
        self.driver = webdriver.Chrome(options=option)  # 实例化Chrome类，并传入option
        self.driver.get("https://work.weixin.qq.com/")  # 打开网页
        self.driver.implicitly_wait(3)  # 隐式等待

    def teardown(self):
        # self.driver.quit()  # 关闭网页
        pass

    def test_debug_login(self):
        self.driver.find_element(By.CSS_SELECTOR, '.index_top_operation a:nth-child(1)').click()  # 获取企业登录按钮元素，并点击
        sleep(2)  # 加一个强制等待，是为了看清中间过程
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#contacts")  # 这里直接复用上面的浏览器，跳过扫描的过程，直接进入到指定的网页
