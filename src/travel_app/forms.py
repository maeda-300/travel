from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from .models import User
from django.utils.translation import gettext_lazy as _

class SignupForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ""

    error_messages = {
        'password_mismatch': _('The two password fields didn’t match.'),
    }
    password1 = forms.CharField(
        label=("パスワード(8文字以上)"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
    )
    password2 = forms.CharField(
        label=("パスワード(確認用)"),
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        strip=False,
    )
    
    class Meta:
        model = User
        fields = ('email','username',)
        labels = {'email':'メールアドレス', 'username':'ユーザー名',}

class LoginForm(AuthenticationForm):

    def __init__(self, request=None, *args, **kwargs):
        super().__init__(request=None, *args, **kwargs)
        self.label_suffix = ""
        self.fields['username'].label = 'メールアドレス'
        