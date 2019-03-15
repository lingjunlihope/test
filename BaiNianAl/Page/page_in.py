"""
    说明：统一入口管理类，主要解决一下两个方面
        1. 对page页面对象统一进行管理
        2. 解决批量导入page问题
        3. 扩展--》解决driver问题
    操作：
        1. 利用类与方法的机制，在统一管理入口类内，新建获取多个页面对象方法
"""
from Base.get_driver import get_driver
from Page.page_address import PageAddress
from Page.page_login import PageLogin

class PageIn():
    def __init__(self):
        self.driver=get_driver()
    # 获取page_login页面对象
    def page_get_login(self):
        return PageLogin(self.driver)
    # 获取page_address页面对象
    def page_get_address(self):
        return PageAddress(self.driver)
