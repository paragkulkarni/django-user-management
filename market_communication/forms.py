from .models import ProductPost
from django import forms


class ProductPostForm(forms.ModelForm):
    class Meta:
        model = ProductPost
        fields = '__all__'
