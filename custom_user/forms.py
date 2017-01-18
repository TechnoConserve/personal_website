from django import forms
from django.utils.translation import ugettext_lazy as _

from wagtail.wagtailusers.forms import UserEditForm, UserCreationForm


class CustomUserEditForm(UserEditForm):
    pass


class CustomUserCreationForm(UserCreationForm):
    pass
