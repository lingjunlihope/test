import allure

import Page
from Base.base import Base

class PageLogin(Base):
    # 点击我
    @allure.step("点击 我")
    def page_click_me(self):
        self.base_click(Page.login_me)
    # 点击 已有账号去登录
    @allure.step("点击 已有账号去登录")
    def page_click_name_ok_link(self):
        self.base_click(Page.login_name_ok_link)
    # 输入用户名
    # @allure.step("输入用户名：%s"%username)
    def page_input_username(self,username):
        allure.attach("输入用户名：%s" %username," ")
        self.base_input(Page.login_username,username)
    # 输入密码
    def page_input_pwd(self,password):
        allure.attach("输入密码：%s"%password," ")
        self.base_input(Page.login_password,password)
    # 点击登录
    @allure.step("点击 登录")
    def page_click_login_btn(self):
        self.base_click(Page.login_btn)
    # 获取昵称 断言
    def page_get_nickname(self):
        # 要先对获取元素文本的方法进行封装   Base
        """注意：必须要加return  把获取到的文本返给调用者"""
        return self.base_get_text(Page.login_nickname)
    # 点击设置
    @allure.step("点击 设置")
    def page_click_setting(self):
        self.base_click(Page.login_setting)
    # 滑动 消息推送-》修改密码
    @allure.step("滑动 消息推送-》修改密码 ")
    def page_drag_and_drop(self):
        # 滑动为公共方法，也需要在Base内封装
        # 定位 消息推送
        el1=self.base_find_element(Page.login_msg_send)
        # 定位 修改密码
        el2=self.base_find_element(Page.login_modify_pwd)
        # 调用base 滑动方法
        self.base_drag_and_drop(el1,el2)
    # 点击退出按钮
    @allure.step("点击 退出")
    def page_click_exit_btn(self):
        self.base_click(Page.login_logout)
    # 确认退出
    @allure.step("点击 确认退出")
    def page_click_exit_btn_ok(self):
        self.base_click(Page.login_logout_ok)