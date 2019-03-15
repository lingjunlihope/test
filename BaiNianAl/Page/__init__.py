"""
    以下为百年奥莱登录数据：
"""
from selenium.webdriver.common.by import By
# 点击 我
login_me=By.ID,"com.yunmall.lc:id/tab_me"
# 点击 已有账号去登录
login_name_ok_link=By.ID,"com.yunmall.lc:id/textView1"
# 输入用户名
login_username=By.ID,"com.yunmall.lc:id/logon_account_textview"
# 输入密码
login_password=By.ID,"com.yunmall.lc:id/logon_password_textview"
# 点击登录
login_btn=By.ID,"com.yunmall.lc:id/logon_button"
# 昵称
login_nickname=By.ID,"com.yunmall.lc:id/tv_user_nikename"
# 设置
login_setting=By.ID,"com.yunmall.lc:id/ymtitlebar_left_btn_image"
"""从消息推送-->滑到-->修改密码"""
# 修改密码
login_modify_pwd=By.ID,"com.yunmall.lc:id/setting_modify_pwd"
# 消息推送
login_msg_send=By.ID,"com.yunmall.lc:id/setting_notification"
# 退出按钮
login_logout=By.ID,"com.yunmall.lc:id/setting_logout"
# 确认退出
login_logout_ok=By.ID,"com.yunmall.lc:id/ymdialog_right_button"