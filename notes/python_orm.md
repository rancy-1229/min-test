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
