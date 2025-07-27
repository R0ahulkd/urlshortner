from django import forms
from django.contrib.auth.models import User
from .models import URL

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'password']

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        # Set placeholder for floating label behavior
        self.fields['username'].widget.attrs.update({
            'placeholder': ' ',
            'class': 'form-control'  # optional: for consistent styling
        })
        self.fields['password'].widget.attrs.update({
            'placeholder': ' ',
            'class': 'form-control'
        })

class URLForm(forms.ModelForm):
    class Meta:
        model = URL
        fields = ['original_url']
