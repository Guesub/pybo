from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from ..forms import QuestionForm
from ..models import Category, Question

@login_required(login_url='common:login')
def question_create(request):
    """
    pybo 질문등록
    """
    category_list = Category.objects.all()
    categoryName=request.POST.get('dropbox',None)

    if request.method == 'POST': # POST 는 데이터 저장을 처리 후 index로 redirection
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.author=request.user
            question.create_date = timezone.now()
            question.category=categoryName # defalut가 문의글로 되어 있기 때문에 Post에서 받은 값을 저장
            if len(question.content) > 100:
                question.content_summary = question.content[:99]
            else:
                question.content_summary = question.content
            question.save()
            return redirect('pybo:index')
    else: # GET 방식으로  from에 QustionFrom을 담아서 입력 받는 페이지로 Return
        form=QuestionForm()
    
    context={'form':form, 'category_list':category_list}
    return render(request, 'pybo/question_form.html', context)

@login_required(login_url='common:login')
def question_modify(request, question_id):
    """
    질문 수정
    """
    question=get_object_or_404(Question, pk=question_id)

    if request.user != question.author:
        messages.error(request, '수정권한이 없습니다.')
        return redirect('pybo:detail', question_id=question.id)

    if request.method == "POST":
        form=QuestionForm(request.POST, instance=question)
        if form.is_valid():
            question=form.save(commit=False)
            question.author = request.user
            question.modify_date = timezone.now()
            question.save()
            return redirect('pybo:detail', question_id=question.id)
    else:
        form=QuestionForm(instance=question)
    context={'form':form}
    return render(request, 'pybo/question_form.html', context)

@login_required(login_url='common:login')
def question_delete(request, question_id):
    """
    질문 삭제
    """
    question=get_object_or_404(Question, pk=question_id)
    if request.user != question.author:
        messages.error(request, '삭제 권한이 없습니다.')
        return redirect('pybo:detail', question=question.id)
    question.delete()
    return redirect('pybo:index')