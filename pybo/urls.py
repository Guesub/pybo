from collections import namedtuple
from django.urls import path

from .views import base_veiws, question_views, answer_views, comment_views, vote_views

app_name='pybo'
urlpatterns =[
    # name attribute는 별칭으로, 별칭을 사용함에 따라, html에 url 호출 시 하드코딩을 피함. 추후 URL 변경시 유지보수 용이
    
    #base_views.py
    path('', base_veiws.Index, name='index'),
    path('<int:question_id>/', base_veiws.DetailView, name='detail'), 
    
    #question_views
    path('question/create/', question_views.question_create, name='question_create'),
    path('question/modify/<int:question_id>/', question_views.question_modify, name='question_modify'),
    path('question/delete/<int:question_id>/', question_views.question_delete, name='question_delete'),
    
    #answer_views
    path('answer/create/<int:question_id>/', answer_views.answer_create, name='answer_create'),
    path('answer/modify/<int:answer_id>/', answer_views.answer_modify, name='answer_modify'),
    path('answer/delete/<int:answer_id>/', answer_views.answer_delete, name='answer_delete'),

    #comment_views
    path('comment/create/question/<int:question_id>', comment_views.comment_create_question, name='comment_create_question'),
    path('comment/modify/question/<int:comment_id>', comment_views.comment_modify_question, name='comment_modify_question'),
    path('comment/delete/question/<int:comment_id>', comment_views.comment_delete_question, name='comment_delete_question'),
    path('comment/create/answer/<int:answer_id>', comment_views.comment_create_answer, name='comment_create_answer'),
    path('comment/modify/answer/<int:comment_id>', comment_views.comment_modify_answer, name='comment_modify_answer'),
    path('comment/delete/answer/<int:comment_id>', comment_views.comment_delete_answer, name='comment_delete_answer'),

    #vote_views
    path('vote/question/<int:question_id>/', vote_views.vote_question, name="vote_question"),
    path('vote/answer/<int:answer_id>/', vote_views.vote_answer, name="vote_answer"),
]