from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        return self.create_user(email, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255, verbose_name='Имя')
    surname = models.CharField(max_length=255, verbose_name='Фамилия')
    patronymic = models.CharField(max_length=255, blank=True, null=True, verbose_name='Отчество')
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.0, verbose_name='Баланс')
    invested = models.DecimalField(max_digits=10, decimal_places=2, default=0.0, verbose_name='Инвестиции')
    email_verification_token = models.CharField(max_length=255, blank=True, null=True)
    email_verification_token_created_at = models.DateTimeField(null=True, blank=True)
    email_verified = models.BooleanField(default=False)

    is_active = models.BooleanField(default=True, verbose_name='Активный')
    is_staff = models.BooleanField(default=False, verbose_name='Сотрудник')

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name", "surname"]

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
