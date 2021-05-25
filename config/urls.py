"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import handler404
from django.contrib import admin
from django.urls import path, include
from pybo.views import base_views

urlpatterns = [
    path('', base_views.Index, name='index'),
    path('admin/', admin.site.urls),
    path('pybo/', include('pybo.urls')),
    path('common/', include('common.urls')),
]

admin.site.site_header="Qsub Pages" # 로그인 전 "Djanggo 관리" 라는 Text 변경
admin.site.site_title="Qsub Pages" # 로그인 후 상단 배너의 "Djanggo 관리" 라는 Text 변경

handler404 = 'common.views.page_not_found' # handelr404 변수를 설정하면 404 오류 발생시 사용자가 정의한 뷰 함수를 호출 여기선 common/views.py의 page_not_found 함수를 호출