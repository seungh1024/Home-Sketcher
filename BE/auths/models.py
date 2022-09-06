from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin, BaseUserManager
)


# 선호 스타일
select_style_class = (
    
) 
# 선호 색상
select_color_class =(
    
)

# 유저 모델
class User(AbstractBaseUser, PermissionsMixin):
    user_pk = models.AutoField(primary_key=True) # 기본키 인덱스
    user_email = models.CharField(max_length=100, unique=True) # 이메일
    user_password = models.CharField(max_length=25) # 비밀번호
    user_name = models.CharField(max_length=25) # 이름
    user_nickname = models.CharField(max_length=30) # 닉네임
    user_gender = models.IntegerField(null=True) # 0 = 남 / 1 = 여
    user_birth = models.IntegerField() # 생년월일
    user_style = models.CharField(max_length=30, default=0, choices=select_style_class) # 선호 스타일
    user_color = models.CharField(max_length=30, default=0, choices=select_color_class) # 선호 색상
    
    USERNAME_FIELD = 'user_pk' # 기본키

    REQUIRED_FIELDS = [
    'user_email',
    'user_password',
    'user_name',
    'user_nickname',
    'user_gender',
    'user_birth',
    ]
    
    def __str__(self):
        return self.user_id