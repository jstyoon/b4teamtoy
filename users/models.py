from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

# custom user model 사용 시 UserManager 클래스와 create_user, create_superuser 함수가 정의되어 있어야 함

class UserManager(BaseUserManager):
    def create_user(self, email, nickname, is_seller, password=None):

        if not email:
            raise ValueError('사용자 이메일은 필수 입력 사항 입니다.')
        if not password:
            raise ValueError('사용자 비밀번호는 필수 입력 사항 입니다.')
        if not nickname:
            raise ValueError('사용자 별명은 필수 입력 사항 입니다.')
        if is_seller == None:
            raise ValueError('사용자 판매/일반 회원 여부는 필수 선택 사항 입니다.')

        user = self.model(
            email=self.normalize_email(email),
            nickname=nickname,
            is_seller=is_seller,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    # python manage.py createsuperuser 사용 시 해당 함수가 사용됨
    def create_superuser(self, email, username, nickname, is_seller, password=None):
        user = self.create_user(
            email,
            password=password,
            username=username,
            nickname=nickname,
            is_seller=is_seller,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

# name, password, nickname, email, follow, created_at, updated_at, signout_at, is_active, is_seller


class User(AbstractBaseUser):
    username = models.CharField("사용자 이름", max_length=20)
    password = models.CharField("비밀번호", max_length=128)  # max?
    nickname = models.CharField("닉네임", max_length=20, unique=True)
    email = models.EmailField("이메일 주소", max_length=100, unique=True)
    created_at = models.DateTimeField("가입일", auto_now_add=True)
    updated_at = models.DateTimeField("수정일", auto_now=True)
    signout_at = models.CharField("탈퇴일", blank=True, max_length=20)
    is_seller = models.BooleanField(default=True)
    followings = models.ManyToManyField(
        'self', symmetrical=False, related_name='followers', blank=True)

    image = models.ImageField(blank=True, upload_to="%Y/%m")
    status_message = models.CharField(
        max_length=50, default="아직 상태 메시지가 없습니다.")

    # is_staff에서 해당 값 사용
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)


    # id로 사용 할 필드 지정.
    # 로그인 시 USERNAME_FIELD에 설정 된 필드와 password가 사용된다.\
    USERNAME_FIELD = 'nickname'
    # USERNAME_FIELD = 'username'

    # user를 생성할 때 입력받은 필드 지정
    REQUIRED_FIELDS = ['username', 'email', 'is_seller']
    objects = UserManager()  # custom user 생성 시 필요

    def __str__(self):
        return self.username

    # 로그인 사용자의 특정 테이블의 crud 권한을 설정, perm table의 crud 권한이 들어간다.
    # admin일 경우 항상 True, 비활성 사용자(is_active=False)의 경우 항상 False
    def has_perm(self, perm, obj=None):
        "사용자에게 특정 권한이 있습니까?"
        return True

    # 로그인 사용자의 특정 app에 접근 가능 여부를 설정, app_label에는 app 이름이 들어간다.
    # admin일 경우 항상 True, 비활성 사용자(is_active=False)의 경우 항상 False
    def has_module_perms(self, app_label):
        "사용자에게 'app_label' 앱을 볼 수 있는 권한이 있습니까?"
        return True

    @property
    def is_staff(self):
        "사용자가 직원입니까?"
        return self.is_admin

    # is_seller 권한 설정
    # @property
    # def is_selleruser(self):
    #     return self.is_seller


