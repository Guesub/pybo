from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

app_name='common'

urlpatterns=[
    #as_view() 괄호 안에 template_name을 사용하여 login.html을 참조할 위치를 정해 줄 수 있다.
    path('login/', auth_views.LoginView.as_view(template_name='common/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name="logout"),
    path('singup/', views.signup, name="signup"),
    path('userprofile/', views.userprofile, name="userprofile"),
    path('changePW/', views.changePW, name="changePW"),
    path('kakaoLogin/', views.kakaoLogin, name="kakaoLogin"),
    path('kakaoOauth/', views.kakaoOauth, name="kakaoOauth"),
    path('logoutPre/', views.logoutPre, name='logoutPre')
]