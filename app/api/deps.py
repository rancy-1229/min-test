from app.core.pq_db  import engine
from collections.abc import Generator
from sqlmodel import Session


# db依赖注入，fastapi路由用Depends(get_db)
def get_db() -> Generator[Session, None, None]:
    with Session(engine) as session:
        yield session
