from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver1=None):  # 参数化传入driver1，默认为None
        if driver1 == None:  # 如果driver1为None就实例化driver
            option = Options()  # 实例化Options类
            option.debugger_address = "localhost:9222"  # 调用debugger_address方法，并传入调试地址为本地启动的一个服务
            self.driver = webdriver.Chrome(options=option)  # 实例化
            self.driver.get("https://work.weixin.qq.com/wework_admin/frame#contacts")  # 打开企业微信的通讯录页面
            self.driver.maximize_window()  # 窗口最大化
        else:
            # 否则self.driver = driver1,self.driver后面的: WebDriver是给self.driver加的类型提示，用于后面好调用该类型的方法，没有任何意义
            self.driver: WebDriver = driver1
        self.driver.implicitly_wait(3)  # 隐式等待

    # 封装self.driver.find_element，提供find方法，并返回；这里需传入连个参数，by-查找的方式，value-具体定位的元素信息
    def find(self, by, value):
        return self.driver.find_element(by, value)

    # 封装显示等待，直到ele元素被选择，时间默认为10s，当前可根据需要更改时间
    def wait_selected(self, ele, time=15):
        return WebDriverWait(self.driver, time).until(expected_conditions.element_to_be_selected(ele))

    # 封装显示等待，直到ele元素可被点击
    def wait_click(self, ele, time=20):
        return WebDriverWait(self.driver, time).until(expected_conditions.element_to_be_clickable(ele))
