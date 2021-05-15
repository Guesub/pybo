from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserForm(UserCreationForm):
    email = forms.EmailField(label="이메일")

    class Meta:
        model=User
        fields =("username", "email")

#UserCreationForm
#은 기본적으로 username과 password1, password2(Password1과 대조하기 위한 값) 을 기본속성으로 가진다.
#Email 속성을 추가하기 위해 UserCreationFrom을 상속하는 UserForm을 새로 만든 것