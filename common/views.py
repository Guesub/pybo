from django.contrib.auth import authenticate, get_user_model, login
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from common.forms import UserForm
from django.contrib import messages

# Create your views here.

def signup(request):
    """
    회원가입
    """
    if request.method =="POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            raw_password=form.cleaned_data.get('password1')
            user=authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form=UserForm()
    return render(request, 'common/signup.html',{'form':form})

# 사용자 프로필 보기
def userprofile(request):

    return render(request, 'common/userprofile.html', None)

# 사용자 패스워드 변경
def changePW(request):

    if request.method=="POST":
        user = User.objects.get(username=request.user.username)
        current_pw=request.POST.get('password', None)
        if check_password(current_pw, user.password):
            new_password1 = request.POST.get('password1', None)
            new_password2 = request.POST.get('password2', None)
            if new_password1 == new_password2:
                user.set_password(new_password1)
                user.save()
                login(request,user)
                messages.info(request, "새로운 비밀번호로 변경 되었습니다.")
                return redirect('index')
            else:
                messages.error(request, "새로운 비밀번호 입력 값이 일치하지 않습니다.")
                return render(request, 'common/userprofile.html', {'PWerror' : 'PWerror'})

        else:
            messages.error(request, "현재 비밀번호가 일치하지 않습니다.")
            return render(request, 'common/userprofile.html', {'PWerror' : 'PWerror'})


def page_not_found(request, exception):
    """
    404 Page not found
    """

    return render(request, 'common/404.html', {})