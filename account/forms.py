from django import forms
from django.forms import ModelForm
from account.models import CustomUser, Score
from django.contrib.auth.hashers import make_password


class CustomUserForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    widget = {
            'password': forms.PasswordInput(),
        }
    class Meta:
        model = CustomUser
        fields = ['image', 'email', 'last_name', 'first_name', 'gender', 'number',  'password']

    def clean_password(self):
        password = self.cleaned_data.get("password",None)
        if self.instance.pk is not None:
            if not password:
                return self.instance.password

        return make_password(password)

class ScoreForm(ModelForm):
    class Meta:
        model = Score
        exclude = ['date_created', 'date_modified']
        