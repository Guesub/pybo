from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect, resolve_url
from django.utils import timezone

from ..forms import AnwserForm
from ..models import Answer, Question

@login_required(login_url='common:login')
def answer_create(request, question_id):
    """
    pybo 답변 등록
    """
    question=get_object_or_404(Question, pk=question_id)

    if request.method=="POST":
        form = AnwserForm(request.POST)
        if form.is_valid():
            answer=form.save(commit=False)
            answer.author=request.user
            answer.create_date=timezone.now()
            answer.question=question
            answer.save()
            return redirect('{}#answer_{}'.format(resolve_url('pybo:detail', question_id=question.id), answer.id ))
            #.resolve_url 함수는 실제 호출되는 URL을 문자열로 반환하는 장고 함수
    else:
        form=AnwserForm()
    context = {'question':question, 'form':form}
    return render(request, 'pybo/question_detail.html', context)

@login_required(login_url='common:login')
def answer_modify(request, answer_id):
    """
    답변 수정
    """
    answer = get_object_or_404(Answer, pk=answer_id)

    if request.user != answer.author:
        messages.error(request, '수정권한이 없습니다.')
        return redirect('pybo:detail', question_id=answer.question.id)

    if request.method=="POST":
        form = AnwserForm(request.POST, instance=answer)
        if form.is_valid():
            answer=form.save(commit=False)
            answer.author=request.user
            answer.modify_date=timezone.now()
            answer.save()
            return redirect('{}#answer_{}'.format(resolve_url('pybo:detail', question_id=answer.question.id), answer.id))
    else:
        form=AnwserForm(instance=answer)
    context={'answer':answer, 'form':form}
    return render(request, 'pybo/answer_form.html', context)

@login_required(login_url='common:login')
def answer_delete(request,answer_id):
    """
    답변 삭제
    """
    answer = get_object_or_404(Answer, pk=answer_id)

    if request.user != answer.author:
        messages.error(request, '삭제 권한이 없습니다.')
        return redirect('pybo:detail', question_id=answer.question.id)
    else:
        answer.delete()
    return redirect('pybo:detail',question_id=answer.question.id)