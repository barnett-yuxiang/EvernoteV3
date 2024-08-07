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

# 尝试注册一个无效用户
invalid_user_data = {
    "username": "tu",
    "email": "invalid-email",
    "password": "short"
}

result = register_user(invalid_user_data)
print(result)

"""
{'status': 'error', 'errors': [{'type': 'string_too_short', 'loc': ('username',), 'msg': 'String should have at least 3 characters', 'input': 'tu', 'ctx': {'min_length': 3}, 'url': 'https://errors.pydantic.dev/2.8/v/string_too_short'}, {'type': 'value_error', 'loc': ('email',), 'msg': 'value is not a valid email address: An email address must have an @-sign.', 'input': 'invalid-email', 'ctx': {'reason': 'An email address must have an @-sign.'}}, {'type': 'string_too_short', 'loc': ('password',), 'msg': 'String should have at least 8 characters', 'input': 'short', 'ctx': {'min_length': 8}, 'url': 'https://errors.pydantic.dev/2.8/v/string_too_short'}]}
"""
