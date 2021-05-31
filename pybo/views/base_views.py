from django.views import generic
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.db.models import Q, Count

from ..models import Answer, Question

import logging

logger = logging.getLogger('pybo')

def Index(request): # request는 사용자가 전달한 데이터를 확인 할 때 사용 된다.

    """
    pybo 목록 출력
    """
    page = request.GET.get('page', '1') # 페이지
    kw = request.GET.get('kw', '')      # 검색어
    so = request.GET.get('so', 'recent')      # 정렬기준

    #정렬
    if so == 'recommend':
        question_list=Question.objects.annotate(num_voter=Count('voter')).order_by('-num_voter', '-create_date')
    elif so == 'popular':
        question_list=Question.objects.annotate(num_answer=Count('answer')).order_by('-num_answer', '-create_date')
    else:
        question_list=Question.objects.order_by('-create_date')

    if kw:
        question_list=question_list.filter(
            Q(subject__icontains=kw) | #제목 검색
            Q(content__icontains=kw) | #내용 검색
            Q(author__username__icontains=kw) | #질문 글쓴이 검색
            Q(answer__author__username__icontains=kw) #답변 글쓴이 검색
            # contains 대신 icontains를 사용하게 되면 대소문자를 가리지 않고 찾아 줌
            # filter 함수에서 모델 필드에 접근하려면 __ 를 이용하면 된다.
        ).distinct() # 중복 제거

    paginator=Paginator(question_list, 10)
    page_obj=paginator.get_page(page)

    context={'question_list':page_obj, 'page':page, 'kw':kw, 'so':so}

    return render(request, 'pybo/question_list.html', context)

def DetailView(request, question_id):
    """
    pybo 내용 출력
    """
    page = request.GET.get('page', '1') # 페이지

    question=Question.objects.get(id=question_id)
        
    answer_list = question.answer_set.all() \
        .annotate(num_voter=Count('voter')) \
        .order_by('-num_voter', '-create_date')

    paginator=Paginator(answer_list, 10)
    page_obj=paginator.get_page(page)

    
    context={'question':question, 'answer_list':page_obj, 'page':page}
    return render(request, 'pybo/question_detail.html', context)