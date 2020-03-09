from django import forms
from .models import Profile, Store, Owner


class StoreForm(forms.ModelForm):
    class Meta:
        model = Store
        fields = '__all__'


class OwnerForm(forms.ModelForm):
    class Meta:
        model = Owner
        fields = '__all__'


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
