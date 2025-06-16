### 类型注入

底层是基于 函数参数的类型注解 + Depends() 自动注入依赖。

```python
from fastapi import Depends, FastAPI

app = FastAPI()

def common_dependency():
    return "hello 注入成功"

@app.get("/test")
def read_item(msg: str = Depends(common_dependency)):
    return {"msg": msg}
```

访问 http://127.0.0.1:8000/test 即可看到返回的结果：

```json
{
    "msg": "hello 注入成功"
}
```

#### 常见类型注入场景

