from pydantic import BaseModel, EmailStr, constr, ValidationError
from typing import List

# 定义 User 模型
class User(BaseModel):
    username: constr(min_length=3, max_length=50)
    email: EmailStr
    password: constr(min_length=8)

# 示例用户数据库
user_db: List[User] = []

# 注册新用户的函数
def register_user(user_data: dict):
    try:
        # 尝试创建 User 对象，这会触发数据验证
        user = User(**user_data)
        
        # 检查用户名是否唯一
        if any(u.username == user.username for u in user_db):
            raise ValueError("Username already exists")
        
        # 添加用户到数据库
        user_db.append(user)
        return {"status": "success", "user": user.dict()}

    except ValidationError as e:
        # 捕获验证错误并返回
        return {"status": "error", "errors": e.errors()}
    except ValueError as e:
        return {"status": "error", "errors": str(e)}

# 测试数据
new_user_data = {
    "username": "testuser",
    "email": "testuser@example.com",
    "password": "securepassword123"
}

# 注册新用户
result = register_user(new_user_data)
print(result)
