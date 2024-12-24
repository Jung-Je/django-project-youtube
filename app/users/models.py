from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager
)
from django.db import models

class UserManager(BaseUserManager):
    # 일반유저 생성 함수
    def create_user(self, email, password):
        if not email:
            raise ValueError("이메일이 맞는지 확인해주세요")
        
        user = self.model(email=email)
        user.set_password(password)
        user.save()

        return user
    
    # 슈퍼유저 생성 함수
    def create_superuser(self, email, password):
        user = self.create_user(email, password)

        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user

class User(AbstractBaseUser, PermissionsMixin):
    email = models.CharField(max_length=255, unique=True)
    nickname = models.CharField(max_length=255)
    is_business = models.BooleanField(default=False)

    #Permissions Mixin: 유저의 권한 관리
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    objects = UserManager()

    def __str__(self):
        return f'email {self.email}, nickname {self.nickname}'