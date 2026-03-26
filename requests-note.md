# HTTP：网站和程序访问服务器的协议

- 网站/程序 ——> HTTP协议 ——> 服务器 ——> 返回数据

# HTTP做了什么：

- 帮你发请求

- 服务器响应

# 请求什么样

- 请求方法：
-          GET：获取数据
-          POST：提交数据
-          PUT:更新数据
-          DELETE：删除数据
- URL：地址
- 请求头：告诉服务器你是谁
- Body：只有POST和PUT有

# 响应是什么：

- 状态码: 200 成功
  404 找不到
  500 服务器错误
  403 禁止访问
- 返回数据

# API(应用程序接口，让你的程序向别人要数据)

- 找URL
- 选方法(GET/POST)
- 传参数(params/json)
- 发请求
- 解析返回json

# 接口分析

- 检查
- network
- Fetch/XHR

- 接口包含：
- URL + Headers(请求头) + 状态码 + 参数 + 请求方法 + 返回数据

# GET 和 POST

- Get不会改变服务器数据，只是获取数据
- Get的params(参数)可以显示在URL上 即 ？后
- POST会改变服务器数据，新增或修改内容
- POST的params不会暴露在URL上
