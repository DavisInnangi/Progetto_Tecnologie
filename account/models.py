from django.core.files.storage import FileSystemStorage
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, AbstractUser, User

COUPONS = {'christmas': 20,
           'easter': 10,
           'epiphany': 5}


class MyAccountManager(BaseUserManager):
    # se si hanno altri required_fields bisogna aggiungerli qui
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("User must have an email address")
        if not username:
            raise ValueError("User must have an username")

        user = self.model(
            email=self.normalize_email(email),
            username=username)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            username=username,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.is_subscribe = 'active'
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    email = models.EmailField(verbose_name='email', max_length=60, unique=True)
    username = models.CharField(max_length=30, unique=True)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)  # aggiunge automaticamente il campo ogni volta
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    stripe_id = models.CharField(max_length=255, default="id_test")
    stripe_subscription_id = models.CharField(max_length=255)
    is_subscribe = models.CharField(max_length=255, default="not_active")
    expire_date = models.DateField(verbose_name='expire date', default='1970-01-01')
    spoiler = models.BooleanField(default=False)
    img = models.ImageField(upload_to='images/', default='images/user_img.png')
    # possiamo aggiungere altri field come il nome o il compleanno

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = MyAccountManager()

    def __str__(self):
        return self.email + ", " + self.username

    def has_perm(self, perm, obj=None):
        return self.is_admin

    @staticmethod
    def has_module_perms(app_label):
        return True
