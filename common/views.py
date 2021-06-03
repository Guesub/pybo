from django.contrib.auth import authenticate, get_user_model, login
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
def userprofile(request, pk):

    User=get_user_model()
    user=get_object_or_404(User, pk=pk)


    if request.user.username != user.username:
        messages.error(request, '조회 권한이 없습니다.')
        return redirect('common:login')

    context = {
        'user' : user
    }

    return render(request, 'common/userprofile.html', context)

def page_not_found(request, exception):
    """
    404 Page not found
    """

    return render(request, 'common/404.html', {})