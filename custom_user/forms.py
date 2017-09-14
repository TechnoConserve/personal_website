from registration.forms import RegistrationForm

from .models import CustomUser


class CustomUserForm(RegistrationForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name'] + RegistrationForm.Meta.fields
