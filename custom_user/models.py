from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils.translation import ugettext_lazy as _


class CustomUserManager(BaseUserManager):
    def create_user(self, email, first_name, password, **kwargs):
        if not email:
            raise ValueError('Users must have a valid email address.')

        if not first_name:
            raise ValueError('Users must supply their first name.')

        if not kwargs.get('username'):
            raise ValueError('Users must have a valid username.')

        user = self.model(email=self.normalize_email(email), first_name=first_name, **kwargs)

        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, first_name, password, **kwargs):
        kwargs.setdefault('is_staff', True)
        kwargs.setdefault('is_superuser', True)
        kwargs.setdefault('is_active', True)

        if kwargs.get('is_staff') is not True:
            raise ValueError(_('Superuser must set is_staff=True.'))
        if kwargs.get('is_superuser') is not True:
            raise ValueError(_('Superuser must set is_superuser=True.'))

        return self.create_user(self.normalize_email(email), first_name, password, **kwargs)


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=40, unique=True)

    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40, null=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = [
        'email',
        'first_name',
    ]

    def __unicode__(self):
        try:
            name = self.get_full_name()
        except TypeError:
            name = self.username
        return name

    def get_full_name(self):
        return ' '.join([self.first_name, self.last_name]).strip()

    def get_short_name(self):
        return self.first_name
