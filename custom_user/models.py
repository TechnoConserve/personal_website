from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models


class CustomUserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, password, **kwargs):
        if not email:
            raise ValueError('Users must have a valid email address.')

        if not first_name:
            raise ValueError('Users must supply their first name.')

        if not last_name:
            raise ValueError('Users must supply their last name.')

        if not kwargs.get('username'):
            raise ValueError('Users must have a valid username.')

        user = self.model(
            email=self.normalize_email(email), username=kwargs.get('username'),
            first_name=first_name, last_name=last_name,
        )

        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, first_name, last_name, password, **kwargs):
        user = self.create_user(email, first_name, last_name, password, **kwargs)

        user.is_superuser = True
        user.save()

        return user


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=40, unique=True)

    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)

    is_superuser = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = [
        'email',
        'first_name',
        'last_name',
    ]

    def __unicode__(self):
        return self.username

    def get_full_name(self):
        return ' '.join([self.first_name, self.last_name])

    def get_short_name(self):
        return self.first_name
