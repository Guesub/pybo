from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

#실거래가 정보를 가지고 오기 위해 필요한 모듈
from urllib.request import urlopen, Request
from urllib import parse
import requests

@login_required(login_url='common:login')
def apttrade(request):
    return render(request, 'pybo/apttrade.html', None)


@login_required(login_url='common:login')
def apttradeinfo(request):
    serviceKey="C0mz/4Z5ocwKxiaIzhh3wgLTzXaqXVOecq8yJ9jnUVWLA5E9VvP0Dy36zP851OOQSKGf8qjS6d9tA2tnnELdTg=="

    url =  'http://openapi.molit.go.kr:8081/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcAptTrade'
    queryParams = parse.urlencode({"ServiceKey" : serviceKey, "LAWD_CD":"11110", "DEAL_YMD": "201512"})
    #queryParams = '?' + parse.urlencode({ parse.quote_plus('ServiceKey') : serviceKey, parse.quote_plus('LAWD_CD') : '11110', parse.quote_plus('DEAL_YMD') : '201512' })
    request = requests.get(url, params=queryParams)

    #request = Request(url+queryParams)

    #request.get_method = lambda: 'GET'
    #response_body = urlopen(request).read()
    print (request.text)