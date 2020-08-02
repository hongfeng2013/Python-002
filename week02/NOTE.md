学习笔记

Homework1:
1. 为 Scrapy 增加代理 IP 功能。
2. 将保存至 csv 文件的功能修改为保持到 MySQL，并在下载部分增加异常捕获和处理机制

主要修改
a. pipelines.py， 将获取的内容保存到mysql
b. middlewares.py, 类RandomHttpProxyMiddleware增加代理


Homework2:
使用 requests 或 Selenium 模拟登录石墨文档 https://shimo.im
主要步骤：
a. 访问'https://shimo.im'。
b. 点击'登录'按钮。
c. 输入用户名/密码。
d. 登录成功后，获取cookies。