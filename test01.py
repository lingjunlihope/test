desc={"name":"张三","age":18}
# 回顾获取字典的值方式 1 通过['键名']
# print(desc['name'])
# print(desc['address'])

# 获取字典值方式2 get(“键名”)方法：
# print(desc.get("name"))
# print(desc.get("address"))


"""
    字典访问方式：
        1. 通过中括号键名 desc['键名']
        2. 通过get(“键名”) 推荐
        区别：get读取不存在的键名，不会报错，值为None
"""
flag=None
if flag:
    print("条件成立！")
else:
    print("条件不成立！")