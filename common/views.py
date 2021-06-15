import json
from django.contrib.auth import authenticate, get_user_model, login
from django.contrib.auth import hashers
from django.contrib.auth import models
from django.contrib.auth.hashers import check_password
from .models import CustomUser
from django.core import exceptions
from django.shortcuts import render, redirect
from common.forms import UserForm
from django.contrib import messages
from django.shortcuts import redirect


from pathlib import Path
import os, json, requests
from django.core.exceptions import ImproperlyConfigured
# Create your views here.

##########  전역 변수  ##########
BASE_DIR = Path(__file__).resolve().parent.parent
secret_file = os.path.join(BASE_DIR, 'secrets.json')
###### 카카오 REST_API_KEY를 가지고 온다 ######
try:
    with open(secret_file) as f:
            secrets=json.loads(f.read())
            REST_API_KEY = secrets["REST_API_KEY"]
            REDIRECT_URI = secrets["REDIRECT_URL"]
except KeyError:
    error_msg="Set the {} environment variable".format("REST_API_KEY")
    raise ImproperlyConfigured(error_msg)
##########################################

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
        user = CustomUser.objects.get(username=request.user.username)
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

def kakaoLogin(request):

    try:
        if request.user.is_authenticated:
            raise KakaoException("User already logged in")
      
        API_HOST = f'https://kauth.kakao.com/oauth/authorize?client_id={REST_API_KEY}&redirect_uri={REDIRECT_URI}&response_type=code'
        f.close()
    except KakaoException as error:
        messages.error(request, error)
        return redirect('index')

    return redirect(API_HOST)


def kakaoOauth(request):
    # 로그인에 성공하게 되면 내가 redirect_uri로 설정한 https://qsub.co.kr/kakaoOauth에
    # code 가 붙어서 오며 이 코드를 가지고 사용자 정보를 얻기 위한 Access Token을 발급 받는다.
    try:
        CODE = request.GET.get('code', None)

        if CODE is None:
            raise KakaoException("Can't get CODE")

        API_HOST = f'https://kauth.kakao.com/oauth/token?grant_type=authorization_code&client_id={REST_API_KEY}&redirect_uri={REDIRECT_URI}&code={CODE}'
        f.close()
        request_access_token=requests.post(API_HOST, headers={"Accept":"application/json"},)
        access_token_json = request_access_token.json()
        error = access_token_json.get("error", None)
        if error is not None:
            print(error)
            KakaoException("Can't get access token")
        
        access_token = access_token_json.get("access_token")

        headers = {"Authorization": f"Bearer {access_token}"}
        user_profile = requests.post("https://kapi.kakao.com/v2/user/me", headers=headers,)

        profile_json = user_profile.json()
        kakao_account = profile_json.get("kakao_account")
        profile = kakao_account.get("profile")

        nickname = profile.get("nickname", None)
        avatar_url = profile.get("profile_image_url", None)
        emailinfo = kakao_account.get("email", None)

        user = CustomUser.objects.get_or_none(email=emailinfo)
        
        if user is None:
            user = CustomUser.objects.create_user(
                email=emailinfo,
                username=emailinfo,
                first_name=nickname,
                login_method=CustomUser.LOGIN_KAKAO,
                access_token= access_token,
                avatar = avatar_url,
            )
            user.set_unusable_password()
            user.save()
        else:
            user.avatar = avatar_url
            user.access_token= access_token
            user.save()


        messages.success(request, "카카오톡 계정을 통하여 로그인 하셨습니다.")
        login(request, user)
        return redirect('index')


    except KakaoException as error:
        messages.error(request, error)
        return redirect('index')

def logoutPre(request):
    try:
        user=CustomUser.objects.get(username=request.user.username)
        access_token = user.access_token
        if access_token is not None:
            user.access_token = None
            user.save()
            headers = {"Authorization": f"Bearer {access_token}"}
            response= requests.post("https://kapi.kakao.com/v1/user/logout", headers=headers)
            print(response)

        return redirect("common:logout")
    except:
        pass

        


# 찾는 페이지가 없는 경우 404 로 이동한다.
def page_not_found(request, exception):
    """
    404 Page not found
    """
    return render(request, 'common/404.html', {})

# 카카오톡 에러처리를 위하여 exceptions을 상속 받은 클래스를 생성해준다.
class KakaoException(Exception):
    pass
