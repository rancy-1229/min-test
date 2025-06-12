
### 安装
```
docker run --name my-postgres -e POSTGRES_PASSWORD=123456 -p 5432:5432 -d postgres
```
### 连接数据库
`
psql -U 用户名
psql -U rancy
`

默认用户名是postgres

#### 创建数据库
```
CREATE DATABASE 数据库名;

CREATE DATABASE shop_db;
```

#### 切换数据库

```
\c shop_db
```

#### 创建表
```
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    email VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```
#### 查看表

```
\dt
```

#### 插入数据

```
INSERT INTO users (username, email) VALUES ('zhanggui', 'boss@example.com');
```

#### 查询数据
```
SELECT * FROM users;
```

条件查询 + 排序
```
SELECT * FROM users WHERE username = 'zhanggui' ORDER BY created_at DESC;
```

更新数据

```
UPDATE users SET email = 'new@example.com' WHERE username = 'zhanggui';
```

删除数据


```
DELETE FROM users WHERE id = 1;
```


### **一、什么是 JSONB？**

- JSONB 是二进制存储的 JSON，比 JSON 更适合查询、索引、过滤。
    
- 存储结构是 **键值对（结构化）+ 索引友好**，适合你保存不规则字段，又想查得快

#### **二、建表 & 插入 JSONB 示例数据**

```
CREATE TABLE products (

    id SERIAL PRIMARY KEY,

    name TEXT,

    attrs JSONB

);
```

```
INSERT INTO products (name, attrs) VALUES

('T恤', '{"color": "red", "size": "L", "tags": ["new", "summer"]}'),

('牛仔裤', '{"color": "blue", "size": "M", "tags": ["sale", "winter"]}');
```

#### **三、JSONB 查询姿势**

 **3.1 查询包含特定 key 和 value**
```
-- 查询 color 为 red 的商品
SELECT * FROM products WHERE attrs ->> 'color' = 'red';
```

 **3.2 查询数组字段包含某个值（tags 里包含 ‘sale’）**
```
SELECT * FROM products 
WHERE attrs -> 'tags' ? 'sale';
```

**3.3 精确匹配整个 JSON 结构**

```
SELECT * FROM products 
WHERE attrs = '{"color": "red", "size": "L", "tags": ["new", "summer"]}';
```

#### **四、JSONB 的索引**

 **4.1 基本 GIN 索引（通用推荐）**
 
```
CREATE INDEX idx_attrs_jsonb ON products USING GIN (attrs);
```

 **4.2 示例：使用** **@>***判断包含（超强匹配）**

```
-- 查询包含 color = red 的 JSON 对象
SELECT * FROM products 
WHERE attrs @> '{"color": "red"}';
```
> @> 是“包含”操作符，意思是 JSON 字段包含右边的结构（key+value）

 **4.3 数组字段查询（包含某个 tag）**
```
-- 查询 tags 中包含 'sale' 的商品
SELECT * FROM products 
WHERE attrs @> '{"tags": ["sale"]}';
```

#### **五、查询字段是否存在**

```
-- 判断是否存在 size 字段
SELECT * FROM products 
WHERE attrs ? 'size';
```

```
-- 判断是否同时存在 color 和 size 字段
SELECT * FROM products 
WHERE attrs ?& array['color', 'size'];
```

#### **六、组合查询（灵活拼接）**

```
SELECT * FROM products 
WHERE attrs @> '{"color": "blue"}'
  AND attrs ->> 'size' = 'M';
```