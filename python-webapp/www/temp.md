## DAY1

## DAY2

## DAY3
ORM的思路就是**把一个表映射成python中的类，行数据映射成类的实例**。

定义了Field字段以后，User表已经具有了表和列的映射信息。


* 参考
[DAY3笔记](http://blog.csdn.net/jyk920902/article/details/78318342)
[github代码](https://github.com/jiyuankai/webapp/blob/master/www/orm.py)



项目后端使用Python3.5编写，基于aiohttp库，并以Jinja2作为模板引擎。使用MySQL数据库。前端部分使用的是uikit CSS框架。
内含自己实现的简易web框架和ORM框架。


后端API：
获取日志：GET /api/blogs
创建日志：POST /api/blogs
修改日志：POST /api/blogs/:blog_id
删除日志：POST /api/blogs/:blog_id/delete
获取评论：GET /api/comments
创建评论：POST /api/blogs/:blog_id/comments
删除评论：POST /api/comments/:comment_id/delete
创建新用户：POST /api/users
获取用户：GET /api/users

管理页面：
评论列表页：GET /manage/comments
日志列表页：GET /manage/blogs
创建日志页：GET /manage/blogs/create
修改日志页：GET /manage/blogs/
用户列表页：GET /manage/users

用户浏览页面：
注册页：GET /register
登录页：GET /signin
注销页：GET /signout
首页：GET /
日志详情页：GET /blog/:blog_id