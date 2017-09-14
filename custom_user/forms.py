from django import forms

from registration.forms import RegistrationForm

from .models import CustomUser


class CustomUserForm(RegistrationForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name'] + RegistrationForm.Meta.fields


class ProfileForm(forms.ModelForm):
    """
    A form for editing user profiles. Assumes that the
    Profile instance passed in has an associated User
    object. The view (see views.py) takes care of that.
    """
    first_name = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'First Name'})
    )
    last_name = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Last Name'})
    )
    email = forms.EmailField(
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Email'})
    )

    class Meta(object):
        model = CustomUser
        fields = ['first_name', 'last_name', 'email']

    def __init__(self, *args, **kwargs):
        # Instance is a CustomUser object
        instance = kwargs.get('instance', None)
        if instance:
            kwargs.setdefault('initial', {}).update({'first_name': instance.first_name,
                                                     'last_name': instance.last_name,
                                                     'email': instance.email})
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        instance = super().save(commit=commit)
        instance.user.first_name = self.cleaned_data['first_name']
        instance.user.last_name = self.cleaned_data['last_name']
        instance.user.email = self.cleaned_data['email']
        if commit:
            instance.user.save()
        return instance
