from django import forms
from .models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('store_name', 'owner_name', 'registered_number', 'address')
