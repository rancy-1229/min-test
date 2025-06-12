#### 目录结构说明
```
.
├── README.md
├── app
│   ├── __init__.py
│   ├── api
│   ├── core
│   ├──  ├──deps.py  # 依赖注入模块
│   ├── env.py
│   ├── main.py # 项目入口






#### 依赖注入模块

deps.py 是 FastAPI 项目中封装公共依赖逻辑（如数据库、权限、用户认证等）的模块，方便在路由层统一注入，形成项目级“中间件”。

#### 项目入口
main.py 是 FastAPI 项目的入口文件，负责初始化 FastAPI 实例、注册路由、启动 uvicorn 服务器。