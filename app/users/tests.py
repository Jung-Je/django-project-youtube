from django.test import TestCase
from django.contrib.auth import get_user_model
# TDD: Test Driven Development (테스트 주도 개발)

class UserTestCase(TestCase):

    # 일반 유저 생성 테스틑 함수
    def test_create_user(self):
        email = 'jung@gmail.com'
        password = 'password123'

        user = get_user_model().objects.create_user(email=email, password=password)

        # 유저가 정상적으로 잘 만들어졌는지 확인
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))
        self.assertFalse(user.is_superuser)

    # 슈퍼 유저 생성 테스트 함수
    def test_create_superuser(self):
        email = 'jung_super@gmail.com'
        password = 'password123'

        user = get_user_model().objects.create_superuser(email=email, password=password)

        # 슈퍼유저인지 확인
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)