#### 什么是ORM？

ORM（Object-Relational Mapping，对象-关系映射）是一种编程技术，它将关系数据库表结构映射到面向对象编程语言中的对象，并通过对象来操纵数据库。
简单来说，将数据库中的表映射为python中的类、字段映射为类属性的技术

可以把生硬的SQL
```
SELECT * FROM users WHERE id = 1;
```

转换为面向对象的代码
```
user = session.query(User).filter_by(id=1).first()
```
#### 主流的Python ORM框架
- SQLAlchemy
- Django ORM
- Peewee
- PonyORM
- SQLObject

#### 为什么要使用ORM？
- 代码更简洁
- 数据库操作更安全
- 数据库操作更方便


### SQLAlchemy 框架执行 SQL 命令

```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker 

# 创建数据库引擎
engine = create_engine('mysql+pymysql://root:123456@localhost:3306/test')       

# 创建会话
Session = sessionmaker(bind=engine)
session = Session()


# 执行 SQL 命令
result = session.execute("SELECT * FROM users WHERE id = 1")
# 打印结果
print(result.fetchall())
```

### alembic 数据库迁移工具

alembic 是一个开源的数据库迁移工具，它可以帮助我们管理数据库的变更，并帮助我们将数据库从一个版本迁移到另一个版本。

alembic 主要有以下几个功能：
- 管理数据库的变更
- 数据库迁移
- 数据库回滚
- 数据库版本控制

#### 安装
1. 安装依赖包
```
pip install alembic
```
2. 初始化alembic
```
alembic init alembic
```
产生目录结构：
```
your_project/
├── alembic.ini          # 主配置文件，数据库连接等配置写这里
├── migrations/          # 存放迁移脚本的目录（默认叫 migrations）
│   ├── env.py           # 核心脚本，运行迁移时会调用这里
│   ├── README           # 一些说明（可无视）
│   ├── script.py.mako   # 自动生成脚本模板
│   └── versions/        # 存放每一次的迁移脚本（一个.py文件一个版本）
```

3. 配置alembic.ini文件(可选)
```
在 alembic.ini 文件中修改数据库连接地址（可以写死，也可以让它读取你的 .env）：
sqlalchemy.url = driver://user:password@host:port/database
```


4. 修改 `alembic/env.py` 文件，动态获取数据库url，并加载模型元数据

```
# alembic/env.py

from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context

# 🚀 导入你自己的模型和数据库配置
from app.models import SQLModel  # 你的模型定义处
from app.core.config import settings  # 存放数据库配置

# 读取 alembic.ini 的配置
config = context.config

# 动态替换数据库连接字符串
config.set_main_option("sqlalchemy.url", settings.SQLALCHEMY_DATABASE_URL)

# 设置元数据（用于自动生成迁移）
target_metadata = SQLModel.metadata
```

保留原有的运行迁移的函数：
```
def run_migrations_offline():
    """Run migrations in 'offline' mode."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )
    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    """Run migrations in 'online' mode."""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)
        with context.begin_transaction():
            context.run_migrations()
```

---

5. 生成迁移脚本

使用自动生成命令来对比模型和数据库差异：

```
alembic revision --autogenerate -m "描述信息"
```

生成的迁移脚本会存放在 `alembic/versions/` 目录下。

#### 6. 应用迁移

```
alembic upgrade head
```

---

#### ⚠️ 注意事项
- `settings.SQLALCHEMY_DATABASE_URL` 是你的配置模块，通常如下：

```python
# app/core/config.py
from pydantic import BaseSettings

class Settings(BaseSettings):
    SQLALCHEMY_DATABASE_URL: str = "sqlite:///./test.db"

settings = Settings()
```

- `alembic.ini` 中的 `sqlalchemy.url` 可以随便写，因为会被 `env.py` 中动态覆盖。
- 若你用 `SQLModel`，建议所有模型都统一继承 `SQLModel` 并在 `env.py` 中导入。
- 自动生成的迁移脚本只会识别表结构变化，不会管字段默认值、校验等 Python 层逻辑。
